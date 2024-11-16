console.log("hola mundo");

var myName = "Jennifer";

function passNmae() {
    return myName;
}

console.log (passNmae);

let greeting = "hola, "+myName+" !"
console.log(greeting)
console.log(typeof greeting)

console.log(greeting.length)
console.log(greeting.indexOf("Jennifer"))

let email = "braismoure@mouredev.com"
console.log(`Hola, ${myName}! Tu email es ${email}`)

console.log(greeting[6])

console.log(greeting.includes("Hola"))
console.log(greeting.includes("Jennifer"))