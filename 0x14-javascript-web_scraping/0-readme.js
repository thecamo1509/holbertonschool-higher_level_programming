#!/usr/bin/node
const Argv = process.argv.slice(2);
const file = require('fs');
file.readFile(Argv[0], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
