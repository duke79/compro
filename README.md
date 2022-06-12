# compro
Competitive programming solutions

# Getting started
```sh
cd src/node
npm i
npm start -- -- 'geeks-for-geeks/reverse-an-array'
```

# To copy over to code ide
```js
const stdio = (main) => {
    // COMMAND TO RUN SO THAT IT WORKS 
    // NEEDS AND INPUT.TXT AND OUTPUT.TXT
    // Get-Content input.txt | node .\solution.js > output.txt
    process.stdin.resume();
    process.stdin.setEncoding("utf-8");

    let standardInputString = "", currentLine = 0;

    function readLine() {
        return standardInputString[currentLine++];
    }

    process.stdin.on("data", rawData => {
        standardInputString += rawData;
    })

    process.stdin.on("end", _ => {
        standardInputString = standardInputString.trim().split("\n").map(line => {
            return line.trim();
        })

        main(readLine);
    })
};

const main = (readLine) => {
    // the exported default function from problem/path.js
};

stdio(main);
```
