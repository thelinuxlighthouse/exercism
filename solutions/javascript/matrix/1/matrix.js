//
// This is only a SKELETON file for the 'Matrix' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Matrix {
  constructor(matrix) {
    this.matrix = matrix
      .split("\n")
      .map(row => row.split(" ").map(Number));
  }

  get rows() {
    // Optional: return copies so callers can’t mutate internal state
    return this.matrix.map(row => row.slice());
  }

  get columns() {
    const rows = this.matrix.length;
    const cols = this.matrix[0].length;

    const result = [];
    for (let c = 0; c < cols; c++) {
      const col = [];
      for (let r = 0; r < rows; r++) {
        col.push(this.matrix[r][c]);
      }
      result.push(col);
    }
    return result;
  }
}
