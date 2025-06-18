let person = {
  name: "Giorgi",
  surname: "Beridze",
  academy: "GOA",
  num: 15,
  favColor: "blue",
  isGoaStudent: true,
  greet: function() {
    console.log("hello");
  }
};

console.log(person);            
console.log(person.name);      
person.greet();            



console.log(true && true);   
console.log(true && false);  
console.log(false && true);  
console.log(false && false);


console.log(true || true);    
console.log(true || false);   
console.log(false || true);  
console.log(false || false);  



let myObj = {
  name: "elene",
  age: 11,
  favColor: "green",
}
  showName: function() {
    console.log(this.name);  
  },

  showAge: function() {
    console.log(this.age);   
  },

  showColor: function() {
    console.log(this.favColor);
};

myObj.showName();
myObj.showAge();
myObj.showColor();
