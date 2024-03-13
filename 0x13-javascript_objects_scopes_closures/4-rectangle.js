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
  
    print () {
      if (this.width === undefined || this.height === undefined) {
        console.log('Invalid dimensions');
        return;
      }
  
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
        console.log('');
      }
    }
  

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
  module.exports = Rectangle;
  