console.log("Hello, World!");

let a =5;
{
    let a = 10;
}
console.log(a); 

let x ="10";
let y = 20;
let z = false;

console.log("5" + 5); // Concatenation, results in "55"
console.log("5" - 5); // Subtraction, results in 0
console.log("5" * 5); // Multiplication, results in 25  
console.log("5" / 5); // Division, results in 1

// use of &&, || and ! operators

let isAdult = true;
let hasID = false;

if (isAdult && hasID) {
    console.log("You can enter the club.");
}
else if (isAdult || hasID) {
    console.log("You can enter the club.");
}
else if (!isAdult) {
    console.log("You are not an adult.");
}

// check if number is positive, negative or zero

let number = 0;

if (number > 0) {
    console.log("The number is positive.");
}
else if (number < 0) {
    console.log("The number is negative.");
}
else {
    console.log("The number is zero.");
}