// 2-7)

// Create an empty object.

// Create an object with your name, age, and city.

// Access the value of a property in an object.

// Add a new property to an existing object.

// Create a nested object (an object inside another object).

// Change the value of an existing property in an object.
// 8-11)

// Check if two numbers are both greater than 10.

// Check if at least one of two conditions is true.

// Use the NOT operator to invert a boolean value.

// Combine multiple logical operations in a single expression.


// 2-7
let emptyObject = {};

let person = {
  name: "Alex",
  age: 30,
  city: "New York"
};

console.log(person.name); 

person.country = "USA";

let employee = {
  id: 101,
  info: {
    name: "Jane Doe",
    department: "Engineering"
  }
};

person.city = "Los Angeles";


// 8-11
public class LogicalOperations {
    public static void main(String[] args) {
        int a = 12;
        int b = 8;
        int x = 5;
        int y = 15;
        boolean isValid = false;
        boolean c = true;

        if (a > 10 && b > 10) {
            System.out.println("a და b ორივე მეტია 10-ზე.");
        }

        if (x > 10 || y > 10) {
            System.out.println("მინიმუმ ერთი პირობა მაინც არის მართალი.");
        }

        if (!isValid) {
            System.out.println("isValid არ არის ჭეშმარიტი (false).");
        }

        if ((a > 10 && b < 10) || !c) {
            System.out.println("კომპლექსური პირობა შესრულდა.");
        }
    }
}
