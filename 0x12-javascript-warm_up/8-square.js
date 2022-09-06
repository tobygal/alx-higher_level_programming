#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
	console.log('Missing size');
} else {
	for (let x = size; x > 0; x--) {
		console.log('X'.repeat(size));
	}
}
