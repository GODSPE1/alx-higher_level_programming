#!/usr/bin/node

const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node script.js <api_url>');
  process.exit(1);
}

// Get the API URL from the command-line argument
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API endpoint
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  } else {
    const films = JSON.parse(body).results;
    const filmFilter = films.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(`${filmFilter.length}`);
  }
});
