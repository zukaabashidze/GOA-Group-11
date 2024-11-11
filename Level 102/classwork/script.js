const wordLengths = new Map([
    ["dad", 0],
    ["aasd", 1],
    ["lusdaa", 2],
    ["luka", 3]
]);

let wordLens = new Set(wordLengths.values());

let sum = 0;
for (let len of wordLens) {
    sum += len;
};

console.log(sum);