#!/usr/bin/node
module.exports = {
  addMeMaybe: function (num, func) {
    return func(num + 1);
  }
};
