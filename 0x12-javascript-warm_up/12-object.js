#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.includes(12)) {
  const updatedArgs = args.map(num => num === 12 ? 89 : num);
  console.log(updatedArgs);
} else {
  console.log(args);
}
