// @ts-check

/**
 * Generates a random starship registry number.
 *
 * @returns {string} the generated registry number.
 */
export function randomShipRegistryNumber(min = 1000, max = 9999) {
  return `NCC-${Math.floor(Math.random() * (max - min) + min)}`;
}

/**
 * Generates a random stardate.
 *
 * @returns {number} a stardate between 41000 (inclusive) and 42000 (exclusive).
 */
export function randomStardate(min = 41000.0, max = 42000.0) {
  return Math.random() * (max - min) + min;
}

/**
 * Generates a random planet class.
 *
 * @returns {string} a one-letter planet class.
 */
export function randomPlanetClass(min = 1, max = 10) {
  let planets = "DHJKLMNRTY";
  let planet = planets[Math.floor(Math.random() * (max - min + 1) + min) - 1];
  return planet;
}
