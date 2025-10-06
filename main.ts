//Main file
console.log("Hello, world!");
console.log("this is a test");
//Meow
let name = "Meow";
//Variables declared with let have block scope, meaning they are accessible only within the block (e.g., if statement, for loop, function) where they are defined. 
//They can be reassigned to a new value.
var age = 24;
//Variables declared with var have function scope, meaning they are accessible within the function where they are defined.
//They can be reassigned to a new value.
const isStudent = true;
//Variables declared with const have block scope, meaning they are accessible only within the block (e.g., if statement, for loop, function) where they are defined.
//They cannot be reassigned to a new value.
if (isStudent) {console.log("You are a student");}
else {console.log("You are not a student");}
//if statements checks if the condition is true, if it is, it will execute the code inside the if statement, if it is false, it will execute the code inside the else statement.
//variables and if statements