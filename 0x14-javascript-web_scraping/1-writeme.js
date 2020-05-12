#!/usr/bin/node
const Argv = process.argv.slice(2);
const file = require('fs');
file.writeFile(Argv[0], Argv[1], err => {
  if (err) {
    console.error(err);
  }
});
