//
// This is only a SKELETON file for the 'Space Age' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const age = (planet, seconds) => {
  let earthSeconds = 31557600;
  let planets = {
      'earth': 31557600,
      'mercury': earthSeconds * 0.2408467,
      'venus': earthSeconds * 0.61519726,
      'mars': earthSeconds * 1.8808158,
      'jupiter': earthSeconds * 11.862615,
      'saturn': earthSeconds * 29.447498,
      'uranus': earthSeconds * 84.016846,
      'neptune': earthSeconds * 164.79132,
    };
  if (!planets.hasOwnProperty(planet)){
    throw('not a planet')
  }
  let years = seconds / planets[planet];
  return  Number(years.toFixed(2))
};
