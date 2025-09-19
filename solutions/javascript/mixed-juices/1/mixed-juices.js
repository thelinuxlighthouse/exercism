// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  switch (name) {
    case "Pure Strawberry Joy":
      return 0.5;
    case "Energizer":
      return 1.5;
    case "Green Garden":
      return 1.5;
    case "Tropical Island":
      return 3;
    case "All or Nothing":
      return 5;
    default:
      return 2.5;
  }
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {
  if (wedgesNeeded === 0 || limes.length === 0){
    return 0;
  }
  let count = 0;
  let i = 0;
  let limesLength = limes.length;
  while (limes.length > 0){
    i++;
    let lime = limes.shift();
    switch (lime){
      case 'small':
        count += 6;
        break;
      case 'medium':
        count += 8;
        break;
      case 'large':
        count += 10;
        break;
    }
    if (count >= wedgesNeeded){
      return i;
    } else if (limes.length === 0){
      return limesLength;
    }
  }
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  let prepareTime = 0;
  while (orders.length >= 0){
    let order = orders.shift();
    switch (order) {
    case "Pure Strawberry Joy":
      prepareTime += 0.5;
      break;
    case "Energizer":
      prepareTime += 1.5;
      break;
    case "Green Garden":
      prepareTime += 1.5;
      break;
    case "Tropical Island":
      prepareTime += 3;
      break;
    case "All or Nothing":
      prepareTime += 5;
      break;
    default:
      prepareTime += 2.5;
      break;
  }
    if(prepareTime >= timeLeft){
      return orders;
    }
  }
}
