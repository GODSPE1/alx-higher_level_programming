#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (width <= 0 || height <= 0 || !Number.isInteger(width) || !Number.isInteger(height)) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
