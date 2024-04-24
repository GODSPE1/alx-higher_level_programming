#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
