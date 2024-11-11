// calculator.js
export function calculate(a, b, op) {
    return op === '+' ? a + b :
           op === '-' ? a - b :
           op === '*' ? a * b :
           op === '/' ? (b !== 0 ? a / b : 'Cannot divide by zero') :
           'Invalid operation';
}

export function filter(arr, func) {
    const result = [];
    for (let item of arr) {
        result.push(func(item));
    }
    return result;
}
