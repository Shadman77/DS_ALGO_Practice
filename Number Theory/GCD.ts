// Ensure both numbers are positive
function findGCD(a: number, b: number): number {
    // Euclidean algorithm to find GCD
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }

    return a;
}

// Example usage
const num1 = 24;
const num2 = 36;

const gcd = findGCD(num1, num2);
console.log(`The GCD of ${num1} and ${num2} is: ${gcd}`);