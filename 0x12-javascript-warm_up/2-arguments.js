#!/usr/bin/node
const numOfArgvs = process.argv.length;
if (numOfArgvs === 2) {
  console.log('No Argument');
} else if (numOfArgvs === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
