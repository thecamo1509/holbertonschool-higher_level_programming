#!/usr/bin/node
const len = process.argv.length;
const convertednumbers = process.argv.slice(2).map(Number);
if (len === 2 || len === 3) {
  console.log(1)
} else {
  const sortedarray = convertednumbers.sort(function (a, b) { return a - b })
  console.log(sortedarray[sortedarray.length - 2])
}
