#!/usr/bin/node

const len = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(len)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
}
