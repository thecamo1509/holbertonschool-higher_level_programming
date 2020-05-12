#!/usr/bin/node
const Argv = process.argv.slice(2);
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + Argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
