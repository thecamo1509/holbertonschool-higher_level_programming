#!/usr/bin/node
function fact (a, b) {
  if (a === 1) {
    return b;
  }
  b *= a;
  return fact(--a, b);
}

const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(fact(num, 1));
}
