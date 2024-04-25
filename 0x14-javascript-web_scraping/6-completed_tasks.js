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
    } else if (response.statusCode === 200) {
        const completed = {};
        const tasks = JSON.parse(body);
        for (const task of tasks) {
            if (task.completed === true) {
                if (completed[task.userId] === undefined) {
                    completed[task.userId] = 1;
                } else {
                    completed[task.userId]++;
                }
            }
        }
        console.log(completed);
    } else {
        console.log(response.statusCode);
    }
});
