#!/usr/bin/node
const Argv = process.argv.slice(2);
const request = require('request');
const file = require('fs');
request(Argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    file.writeFile(Argv[1], body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
