module.exports = (readLine) => {
    let T = parseInt(readLine());
    while (T--) {
        let N = readLine().split(" ");
        let line = readLine().split(" ");
        console.log({ N, line, args: process.argv });
        // let line = readLine().split(" ").map(num => parseInt(num));
    }
};
