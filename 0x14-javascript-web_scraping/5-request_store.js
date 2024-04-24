#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length !== 4) {
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    fs.writeFile(filePath, body, 'utf8', function (err) {
      if (err) {
        console.error('Error writing to file:', err);
      } else {
        console.log(filePath);
      }
    });
  }
});
