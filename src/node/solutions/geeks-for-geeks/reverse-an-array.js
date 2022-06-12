module.exports = (readLine) => {
    let T = parseInt(readLine());
    while (T--) {
        let N = readLine().split(" ");
        let line = readLine().split(" ");
        while(N--) {
            console.log(line[N]);
        }
    }
};
