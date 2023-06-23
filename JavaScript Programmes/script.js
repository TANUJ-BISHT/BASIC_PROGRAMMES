"use strict";
let userinput = prompt("enter number");
//====6 FALSY VALUES IN JS====
// false , 0 , undefined , numm , NaN , ''
// EveryThing except above falsy values when converted to bool
// will be true.

// ====CHECKING ODD OR EVEN NUMBER===
function Check_Odd_Even(userinput) {
  userinput % 2 === 0
    ? console.log("yo even number hai ", userinput)
    : console.log("hat odd hai ", userinput);
}

// ====CHECKING PRIME NUMBER====
function check_prime(userinput) {
  let is_prime = true;
  for (let i = 2; i < userinput; i++) {
    if (userinput % i === 0) is_prime = false;
  }
  //uncommented cuz itz printing in twisted prime :'>
  // is_prime ? console.log(userinput,'is a prime number') :
  // console.log(userinput,'is not a prime number');
  return is_prime;
}

//====CHECKING TWISTED PRIME====
// will be using check_prime for this cuz im lazy :)
function check_twisted_prime(userinput) {
  if (check_prime(userinput)) {
    let temp_num = String(userinput);
    let rev_num_str = "";
    for (let i = 0; i < temp_num.length; i++) {
      rev_num_str = temp_num[i] + rev_num_str;
    }
    if (check_prime(Number(rev_num_str))) {
      console.log(`${userinput} is a twisted prime number`);
    } else {
      console.log(`${userinput} is a not twisted prime number`);
    }
  }
}

//====CHECKING MAGIC NUMBER====
function check_magic(number) {
  let sum = 0;
  let numString = number.toString();
  for (let i = 0; i < numString.length; i++) {
    let digit = parseInt(numString[i]);
    sum += digit;
  }
  if (sum === 1) {
    console.log(`${number} is a magic number`);
  } else if (sum > 9) {
    return check_magic(sum);
  } else {
    console.log(`${number} is not a magic number`);
  }
}

//====CHECKING AMSTRONG NUMBER====
function check_amstrong(number) {
  let sum = 0;
  let temp = number;
  const digits = number.toString().length;

  while (temp > 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  sum === number
    ? console.log(`${number} is an Armstrong number`)
    : console.log(`${number} is not an Armstrong number`);
}

//CHECKING PALLENDROME NUMBER====
function isPalindrome(number) {
  const reverseNumber = parseInt(
    number.toString().split("").reverse().join("")
  );
  number === reverseNumber
    ? console.log(`${number} is a palindrome`)
    : console.log(`${number} is not a palindrome`);
}
//FIBONACCI SERIES
function fibonacci(userinput) {
  let a = 0;
  let b = 1;
  let c = 0;
  while (c <= userinput) {
    c = a + b;
    console.log(a, " + ", b, " = ", c);
    a = b;
    b = c;
  }
}
