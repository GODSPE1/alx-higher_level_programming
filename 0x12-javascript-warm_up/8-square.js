#!/usr/bin/node

let len = parseInt(process.argv[2]);

if (process.argv[2] === undefined || isNaN(len)) {
  console.log('Missing size');
} else {
  let pstr = '';
  for (let i = 0; i < len; i++) {
    pstr += 'X';
  }
  while (len > 0) {
    console.log(pstr);
    len--;
  }
}
