#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !Number.isInterger(w) || !Number.isInteger(h)) {
      return {};
    } else {
      this.width = w;
      this.geight = w;
    }
  }
};
