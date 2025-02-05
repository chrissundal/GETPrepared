

global.setTimeout(() => {
    console.log('in the timeout')
}, 3000);
let num = 1;
const int = setInterval(() => {
    console.log(`${num} of the interval`)
    num ++;
    if (num > 10) {
        clearInterval(int);
    }
},1000);

console.log(__dirname)
console.log(__filename)