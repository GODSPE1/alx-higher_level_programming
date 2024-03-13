#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  print() {
    super.print();
  }

  double() {
    super.double();
  }
}

module.exports = Square;
