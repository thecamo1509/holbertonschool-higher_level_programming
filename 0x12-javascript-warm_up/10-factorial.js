#!/usr/bin/node
function fact (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  }
  return num * fact(--num);
}

const num = parseInt(process.argv[2], 10);
const result = fact(num);
console.log(result);
