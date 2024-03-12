#!/usr/bin/node

const myVar = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(myVar)) {
  console.log('Not a Number');
} else {
  console.log('My number: ' + myVar);
}
