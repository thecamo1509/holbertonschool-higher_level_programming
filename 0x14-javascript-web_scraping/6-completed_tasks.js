#!/usr/bin/node
const Argv = process.argv.slice(2)
const request = require('request');
const mydict = {};
request.get(Argv[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    for (const tasks of (JSON.parse(body))) {
      if (tasks.completed) {
        if (!mydict[tasks.userId]) {
          mydict[tasks.userId] = 1;
        } else {
          mydict[tasks.userId]++;
        }
      }
    }
    console.log(mydict);
  }
});
