#!/usr/bin/node
const Argv = process.argv.slice(2);
const request = require('request');
let id = 0;
let count = 0;
const mydict = {};
request(Argv[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    id = body[0].userId;
    for (let i = 0; i < body.length; i++) {
      if (body[i].userId !== id) {
        mydict[id.toString()] = count;
        id = body[i].userId;
        count = 0;
      }
      if (body[i].completed === true) {
        count++;
      }
    }
    mydict[id.toString()] = count;
    console.log(mydict);
  }
});
