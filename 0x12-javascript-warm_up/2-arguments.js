#!/usr/bin/node
import { argv } from 'node:process';
if (!argv) {
  console.log('No Argument');
} else if (argv.length === 1) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
