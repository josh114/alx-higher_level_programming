#!/usr/bin/node
const numOfArgvs = process.argv.length;
if (numOfArgvs === 2) {
  console.log('No argument');
} else if (numOfArgvs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
