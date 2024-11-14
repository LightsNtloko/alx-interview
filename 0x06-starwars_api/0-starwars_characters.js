#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL with the movie ID to fetch data from the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  
  // Parse the JSON response body
  const data = JSON.parse(body);
  
  // Extract the list of character URLs and fetch each character’s name
  const characters = data.characters;
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }
      
      // Parse character data and log the name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

