#!/usr/bin/node

const args = process.argv;
if (args <= 2) {
  console.log(0);
} else {
let largest = Number.NEGATIVE_INFINITY;
let secondLargest = Number.NEGATIVE_INFINITY;

for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (!isNaN(num)) {
        if (num > largest) {
            secondLargest = largest;
            largest = num;
        } else if (num > secondLargest && num !== largest) {
            secondLargest = num;
        }
    }
}

console.log(secondLargest !== Number.NEGATIVE_INFINITY ? secondLargest : 0);
}

