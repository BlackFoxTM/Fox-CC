
var invalid = "The Card Number is Invalid ! ";
var undetermined = "please , enter more digits";

var mc = "MasterCard";
var visa = "Visa";
var amex = "American Express";
var diners = "Diners Club / Carte Blanche";
var dinersint = "Diners Club / International";
var discover = "Discover"
var er = "Diners Club / enRoute";
var jcb = "JCB";

function GetBank(numb) {

  // 51-55 mc
  // 4     visa
  // 34, 37amex
  // 300-305     diners carte blanche
  // 36, 38diners int
  // 6011  discover
  // 2014, 2149  er
  // 3     jcb
  // 2131, 1800  jcb

  var bank = "???";
  var prefix;
  if (numb.length == 0) { // nothing entered yet
    bank = "";
  } else if (numb.charAt(0) > 6) { // 1st digit is 7, 8, or 9
    bank = invalid;
  } else if (numb.charAt(0) == "4") { // 1st digit is 4
    bank = visa;
  } else if (numb.length == 1) { // one digit entered
    bank = undetermined;
  } else if (numb.length >= 2) { // two or more digits entered
    if (numb.substr(0,2) >= "51" && numb.substr(0,2) <= "55") { // 1st 2 digits are 51-55
      bank = mc;
    } else if (numb.charAt(0) == "3") { // first digit is 3
      if (numb.charAt(1) == "4" || numb.charAt(1) == "7") { // 1st 2 digits are 34 or 37
        bank = amex;
      } else if (numb.charAt(1) == "6") { // 1st 2 digits are 36 or 36
        bank = dinersint;
      } else if (numb.charAt(1) == "6") { // 1st 2 digits are 36 or 38
        bank = diners;
      } else if (numb.length == 2) { // exactly two digits entered starting with a 3
        if (numb.charAt(1) == "0") { // 1st 2 digits are 30
          bank = undetermined;
        } else {
          bank = jcb;
        }
      } else if (numb.substr(1,2) >= "00" &&
                 numb.substr(1,2) <= "05") { // 1st 3 digits are 300-305
        bank = diners;
      } else { // 1st digit is 3 and none of the special cases for 3 apply
        bank = jcb;
      }
    } else if (numb.length == 2) { // exactly 2 digits
      prefix = numb.substr(0,2);
      if (prefix != "30" && prefix != "60" && // 30 is for diners, 60 is for discover
          prefix != "20" && // for enRoute
          prefix != "21" && prefix != "18") {
         // doesn't start with any remaining allowable sequence
        bank = invalid;
      } else { // need more than 2 digits to determine the bank
        bank = undetermined;
      }
    } else if (numb.length == 3) { // exactly 3 digits
      prefix = numb.substr(0,3);
      if (prefix != "601" &&
          prefix != "201" && prefix != "214" && // for enRoute 
          prefix != "213" && prefix != "180") {
        // doesn't start with any remaining allowable sequence
        bank = invalid;
      } else { // need more than 3 digits to determine the bank
        bank = undetermined;
      }
    } else if (numb.length >= 4) { // 4 or more digits
      prefix = numb.substr(0,4);
      if (prefix == "6011") { // first 4 digits are 6011
        bank = discover;
      } else if (prefix == "2131" || prefix == "1800") { // first 4 digits are 2131 or 1800
        bank = jcb;
      } else if (prefix == "2014" || prefix == "2149") { // first 4 digits are 2014 or 2149
        bank = er;
      } else { // nothing left, it's invalid
        bank = invalid;
      }
    }
  }
  return bank;
}

function GetLength(numb, bank) {
  if (bank == mc) return 16;
  if (bank == visa) return 16; // could also be 13 ??? -- obsolete
  if (bank == amex) return 15;
  if (bank == diners) return 14;
  if (bank == dinersint) return 14;
  if (bank == discover) return 16
  if (bank == er) return 15;
  if (bank == jcb) {
    if (numb.charAt(0) == "3") return 16; else return 15;
  }
  return 0;
}

function Validate(numb, bank) {
  var len = GetLength(numb, bank);

  if (len == 0) { // means too few digits for validity to be determined
    return "";
  }

/* drop this because 13 digit visa numbers are now obsolete
  if (bank == visa) { // special case because it could be 13 or 16 digits
    if (numb.length < 13 || numb.length == 14 || numb.length == 15) {
      return "enter more digits"
    } else if (numb.length > 16) {
      return "*** TOO MANY DIGITS ***";
    }
  } else
*/
  if (numb.length < len) {
    result = "enter more digits"
  } else if (numb.length > len) {
    result = "*** TOO MANY DIGITS ***";
  } else if (bank == er) { // special case because enRoute numbers do not have a checksum
    result = "number is valid";

  } else {

    var odd = true;
    var sum = 0;
    var temp;
    var mult;
    var result = "";
    for (var i=numb.length-1; i>=0; i--) {
      mult = odd ? 1 : 2;
      temp = mult * numb.charAt(i);
      odd = !odd;
      if (temp > 9) {
        temp -= 9; // a clever way to add the sum of the digits
      }
      sum -= (-temp);
    }
    if (sum%10 == 0) {
      result = "The Card Number is Valid";
    } else {
      result = "The Card Number is Invalid !";
    }
  }

  if (result != "number is valid" && result != "enter more digits") {
    //pass
  } else {

    //pass
  }
  return result;
}

const numb = process.argv[2]



console.log("Your Card Number is : " + numb + "\n\n")
const bank = GetBank(numb);
console.log("Type is : " + bank);
const result = Validate(numb,bank);
console.log(result);

