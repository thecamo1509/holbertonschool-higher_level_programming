#!/usr/bin/node
exports.callMeMoby = function (a, b) {
  let i = 0;
  while (i < a) {
    b();
    i++;
  }
};
