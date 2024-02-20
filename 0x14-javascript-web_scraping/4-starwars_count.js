#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const characterId = '18'; // Wedge Antilles' character ID
      const numMovies = films.filter(film =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
      console.log(numMovies);
    }
  }
});
