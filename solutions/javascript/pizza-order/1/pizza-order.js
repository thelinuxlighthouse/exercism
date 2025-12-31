/// <reference path="./global.d.ts" />
//
// @ts-check

/**
 * Determine the price of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
export function pizzaPrice(pizza, ...extras) {
  let pizzaPrice = 0;
  const pizzaTypes = {
    Margherita: 7,
    Caprese: 9,
    Formaggio: 10,
  };
  const pizzaToppings = {
    ExtraSauce: 1,
    ExtraToppings: 2,
  }
  pizzaPrice += pizzaTypes[pizza];
  for (const extra of extras) {
    if (extra === "ExtraSauce") {
      pizzaPrice += 1;
    } else if (extra === "ExtraToppings") {
      pizzaPrice += 2;
    }
  }
  return pizzaPrice;
}

/**
 * Calculate the price of the total order, given individual orders
 *
 * (HINT: For this exercise, you can take a look at the supplied "global.d.ts" file
 * for a more info about the type definitions used)
 *
 * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
 * @returns {number} the price of the total order
 */
export function orderPrice(pizzaOrders) {
  let total = 0;

  for (const order of pizzaOrders) {
    // Calculate price for each pizza order
    total += pizzaPrice(order.pizza, ...order.extras);
  }

  return total;
}
