#!/usr/bin/node
function factorial (factor) {
  if (isNaN(factor) || factor === 0) {
    return 1;
  } else {
    return factor * factorial(factor - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
