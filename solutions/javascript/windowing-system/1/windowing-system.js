// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */

export class Size {
  constructor(width = 80, height = 60) {
    this.width = width;
    this.height = height;
  }

  resize(newWidth, newHeight) {
    this.width = newWidth;
    this.height = newHeight;
  }
}

export class Position {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
  }

  move(newX, newY) {
    this.x = newX;
    this.y = newY;
  }
}

export class ProgramWindow {
  constructor() {
    this.screenSize = new Size(800, 600);
    this.size = new Size();
    this.position = new Position();
  }

  resize(newSize) {
    // minimum size is 1x1
    const requestedWidth = Math.max(1, newSize.width);
    const requestedHeight = Math.max(1, newSize.height);

    // maximum size depends on current position (must still fit on screen)
    const maxWidth = this.screenSize.width - this.position.x;
    const maxHeight = this.screenSize.height - this.position.y;

    const finalWidth = Math.min(requestedWidth, maxWidth);
    const finalHeight = Math.min(requestedHeight, maxHeight);

    this.size.resize(finalWidth, finalHeight);
  }

  move(newPosition) {
    // minimum position is (0,0)
    const requestedX = Math.max(0, newPosition.x);
    const requestedY = Math.max(0, newPosition.y);

    // maximum position depends on current size (must still fit on screen)
    const maxX = this.screenSize.width - this.size.width;
    const maxY = this.screenSize.height - this.size.height;

    const finalX = Math.min(requestedX, maxX);
    const finalY = Math.min(requestedY, maxY);

    this.position.move(finalX, finalY);
  }
}


export function changeWindow(programWindow) {
  programWindow.move(new Position(100, 150));
  programWindow.resize(new Size(400, 300));
  return programWindow;
}