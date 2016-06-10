

import java.lang.reflect.Method;
// Write a single generic function named printArray; 
// this function must take an array of generic elements as a parameter (the exception to this is C++, which takes a vector). 
// The locked Solution class in your editor tests your function.

class Solution {

	 public static < E > void printArray(E[] arrayList){

	 	 for(E i : arrayList ){
        System.out.println(i) ;
    }
    
    
    
}
    public static void main(String args[]){
        Integer[] intArray = { 1, 2, 3 };
        String[] stringArray = { "Hello", "World" };
        
        printArray( intArray  );
        printArray( stringArray );
        
        if(Solution.class.getDeclaredMethods().length > 2){
            System.out.println("You should only have 1 method named printArray.");
        }
    }
}