#!/usr/bin/node
// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the film ID from the command line argument (process.argv[2])
const filmId = process.argv[2];

// Construct the URL for the Star Wars movie using the provided filmId
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

// Make a GET request to retrieve film data
request(url, async function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        // Parse the response body as JSON
        const filmData = JSON.parse(body);

        // Extract the characters array from the film data
        const characters = filmData.characters;

        // Iterate through each character and fetch their name
        for (const character of characters) {
            // Create a Promise to handle the asynchronous request
            const res = await new Promise((resolve, reject) => {
                // Make a GET request to the character URL
                request(character, (error, response, body) => {
                    if (error) {
                        reject(error);
                    } else {
                        // Parse the character data and resolve with the character's name
                        resolve(JSON.parse(body).name);
                    }
                });
            });
            // Print the name of the character
            console.log(res);
        }
    }
});
