#!/usr/bin/node

function add (a, b) {
    return (a + b);
}
if (process.argv.lenght < 4) {
    console.log('NaN')
} else {
    console.log(add(parseInt(process.argv[2]), add(parseInt(process.argv[3])));
}