/// <reference path="./global.d.ts" />
// @ts-check
//
// The lines above enable type checking for this file. Various IDEs interpret
// the @ts-check and reference directives. Together, they give you helpful
// autocompletion when implementing this exercise. You don't need to understand
// them in order to use it.
//
// In your own projects, files, and code, you can play with @ts-check as well.

export class TranslationService {
  /**
   * Creates a new service
   * @param {ExternalApi} api the original api
   */
  constructor(api) {
    this.api = api;
  }

  /**
   * Attempts to retrieve the translation for the given text.
   *
   * - Returns whichever translation can be retrieved, regardless the quality
   * - Forwards any error from the translation api
   *
   * @param {string} text
   * @returns {Promise<string>}
   */
  free(text) {
    return this.api.fetch(text).then((result) => result.translation);
  }

  /**
   * Batch translates the given texts using the free service.
   *
   * - Resolves all the translations (in the same order), if they all succeed
   * - Rejects with the first error that is encountered
   * - Rejects with a BatchIsEmpty error if no texts are given
   *
   * @param {string[]} texts
   * @returns {Promise<string[]>}
   */
  batch(texts) {
    if (texts.length === 0) {
      return Promise.reject(new BatchIsEmpty());
    }
    const promises = texts.map((t) => this.free(t));
    return Promise.all(promises);
  }

  /**
   * Requests the service for some text to be translated.
   *
   * Note: the request service is flaky, and it may take up to three times for
   *       it to accept the request.
   *
   * @param {string} text
   * @returns {Promise<void>}
   */
  request(text) {
    return new Promise((resolve, reject) => {
      const attempt = (attemptsLeft) => {
        try {
          this.api.request(text, (err) => {
            if (err === undefined) {
              // success
              resolve();
              return;
            }

            // failure
            if (attemptsLeft > 1) {
              attempt(attemptsLeft - 1);
            } else {
              reject(err);
            }
          });
        } catch (e) {
          // api.request can throw (e.g. abusive client); forward it
          reject(e);
        }
      };

      attempt(3);
    });
  }

  /**
   * Retrieves the translation for the given text
   *
   * - Rejects with an error if the quality can not be met
   * - Requests a translation if the translation is not available, then retries
   *
   * @param {string} text
   * @param {number} minimumQuality
   * @returns {Promise<string>}
   */
  premium(text, minimumQuality) {
  return this.api.fetch(text)
    .then(({ translation, quality }) => {
      // Fetch succeeded → check quality
      if (quality < minimumQuality) {
        throw new QualityThresholdNotMet(text);
      }
      return translation;
    })
    .catch((error) => {
      // If translation exists but quality was too low,
      // do NOT request again
      if (error instanceof QualityThresholdNotMet) {
        throw error;
      }

      // Otherwise, translation was NOT available → request it
      return this.request(text).then(() =>
        this.api.fetch(text).then(({ translation, quality }) => {
          if (quality < minimumQuality) {
            throw new QualityThresholdNotMet(text);
          }
          return translation;
        })
      );
    });
}
}

/**
 * This error is used to indicate a translation was found, but its quality does
 * not meet a certain threshold. Do not change the name of this error.
 */
export class QualityThresholdNotMet extends Error {
  /**
   * @param {string} text
   */
  constructor(text) {
    super(
      `
The translation of ${text} does not meet the requested quality threshold.
    `.trim(),
    );

    this.text = text;
  }
}

/**
 * This error is used to indicate the batch service was called without any
 * texts to translate (it was empty). Do not change the name of this error.
 */
export class BatchIsEmpty extends Error {
  constructor() {
    super(
      `
Requested a batch translation, but there are no texts in the batch.
    `.trim(),
    );
  }
}
