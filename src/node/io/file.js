const fs = require('fs');

const file = (file_path, main) => {
    try {
        const data = fs.readFileSync(file_path, 'utf8');
        const lines = data.split(/\r?\n/);
        let idx = 0;
        const readline = () => {
            const ret = lines[idx];
            idx++;
            return ret; 
        };
        main(readline);
      } catch (err) {
        console.error(err);
      }
};

module.exports = {
    file,
};
