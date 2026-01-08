//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const decodedValue = (colors) => {
        let sum = '';
        let [a, b] = colors;
        sum = COLORS.indexOf(a).toString() + COLORS.indexOf(b).toString();
        return Number(sum);
}

export const COLORS = [
      'black',
      'brown',
      'red',
      'orange',
      'yellow',
      'green',
      'blue',
      'violet',
      'grey',
      'white',
    ];

