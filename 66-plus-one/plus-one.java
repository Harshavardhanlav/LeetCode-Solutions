class Solution {
   public static int[] plusOne(int[] digits) {
        int i = digits.length-1;

        while(i >= 0) {
            if(digits[i] == 9) {
                digits[i] = 0;
      
                
            } else {
                digits[i] += 1;
   
                return digits;
            }
            i--;
        
        }
        int[] new_arr = new int[digits.length+1];
        new_arr[0] = 1;
        int index = 1;
        for(int j : digits) {
            new_arr[index] = j;
            index++;
        }
        return new_arr;
    
    
    }
}