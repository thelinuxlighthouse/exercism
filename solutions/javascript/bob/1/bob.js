//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export function hey(message) {
  const msg = message.trim();

  // Silence
  if (msg === '') {
    return 'Fine. Be that way!';
  }

  const isQuestion = msg.endsWith('?');

  const hasLetters = /[a-zA-Z]/.test(msg);
  const isYelling = hasLetters && msg === msg.toUpperCase();

  // Yelling question
  if (isYelling && isQuestion) {
    return "Calm down, I know what I'm doing!";
  }

  // Yelling
  if (isYelling) {
    return 'Whoa, chill out!';
  }

  // Question
  if (isQuestion) {
    return 'Sure.';
  }

  // Anything else
  return 'Whatever.';
}
