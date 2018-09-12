// Math 1
// Write a function called zero_negativity(). This function should take an array. Return true if the input array contains no negative numbers, return false if it does.
//
// Math 2
// Write a function called is_even(). This function should take a number. Return true if the input number is even, return false if the number is odd.
//
// Math 3
// Write a function called how_many_even(). This function should take an array. Return the total number of elements in the array that are even. You may call is_even() to solve this.
//
// Math 4
// Write a function called create_dummy_array(). This function should take a number n. Return an array of random numbers between 0 and 9 with the length of n.
//
// Math 5
// Write a function called random_choice(). This function should take an array. Return a random element of the array, based on its length. This function should never return undefined.

// function zero_negativity(arr){
//    for (let i=0; i<arr.length;i++){
//       if( arr[i]<0){
//          return "false";
//       }
//    }
//    return "true"
// };
// let x = zero_negativity([1,23,11,15,-12]);
// let y =zero_negativity([22,1,15,93])
// console.log(x);
// console.log(y);

function is_even(num){
   if( num % 2 === 0){
      return "true"
   } else {
      return "false"
   }
};

// let x= is_even(12)
// let y= is_even(31)
// console.log(x);
// console.log(y);

function how_many_even(arr){
   let sum =0;
   for(let i=0;i < arr.length;i++){
      if (is_even(arr[i])=== "true"){
         sum+=1;
      }
   }
   return sum;
}
let x = how_many_even([12,44,13,18,45,76]);
let y = how_many_even([19,41,13,18,45,76]);
console.log(x);
console.log(y);
