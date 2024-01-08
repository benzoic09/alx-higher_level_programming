#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];

const num1 = Number(arg1);
const num2 = Number(arg2);

if (!isNaN(num1) && !isNaN(num2)) {
  console.log(add(num1, num2));
} else {
  console.log('Invalid input. Please provide two integers.');
}
