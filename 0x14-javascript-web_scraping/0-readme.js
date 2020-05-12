#!/usr/bin/node
const Argv = process.argv.slice(2);
const file = require('fs');
file.readFile(Argv[0], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
