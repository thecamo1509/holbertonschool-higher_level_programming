#!/usr/bin/node
let i = 0

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size')
} else {
  while (i < process.argv[2]) {
    console.log('X'.repeat(parseInt(process.argv[2])))
    i++
  }
}
