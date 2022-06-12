const { stdio } = require('./io/stdio');
const { file } = require('./io/file');
const { exit } = require('process');

const problem_path = process.argv[2];
if (!problem_path) {
    console.error(`Run command with valid problem name.`);
    console.error(`eg. \n\n\n "npm start -- -- 'geeks-for-geeks/reverse-an-array'" \n\n\n`);
    exit(0);
}

const file_path = '../../sample-input/' + problem_path + '.txt';
const solution_path = './solutions/' + problem_path + '.js';
const main = require(solution_path);

console.log('Output starts here\n--------------------------------');
// stdio(main);
file(file_path, main);
console.log('--------------------------------\nOutput ends here');