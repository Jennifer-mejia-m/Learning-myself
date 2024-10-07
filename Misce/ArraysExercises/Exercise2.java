package ArraysExercises;

public class Exercise2 {
  
    public static void main(String[] args) {
       
    int[] myArray = {
        5,8,6,12,9,74,22,3,4    
    };
        
    int sum = 0;

    //itera sobre el índice

    //for (int i = 0; i < myArray.length; i++) {
        //sum += i;
    //}

    System.out.println(sum);

    //itera sobre los valores del array

    for (int i : myArray) {
        sum += i;
    }

    System.out.println(sum);

    }
}
