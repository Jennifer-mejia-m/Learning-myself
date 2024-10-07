package ArraysExercises;

public class Exercise3 {
    
    public static void main(String[] args) {
        
        int [] myArray = {
            3,4,5,6,7,9,2,37
        };

        double sum = 0;

        double largo = myArray.length;

        for (int i : myArray) {
            sum += i;
        }

        double average = sum/largo;

        System.out.println(Math.round(average*100d)/100d);
     
    }
}
