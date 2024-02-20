#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', function (err) {
    console.log(`${filePath}`);
  });
});
