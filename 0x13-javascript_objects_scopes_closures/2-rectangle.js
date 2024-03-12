#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0 || !Number.isInteger(width) || !Number.isInteger(height)) {
      // Create an empty object
      this.width = undefined;
      this.height = undefined;
    } else {
      // Initialize the instance attributes width and height
      this.width = width;
      this.height = height;
    }
  }
}

module.exports = Rectangle;
