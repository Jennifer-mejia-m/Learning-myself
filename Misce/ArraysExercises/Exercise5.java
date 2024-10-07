package ArraysExercises;

public class Exercise5 {

    //Calcular el mínimo y máximo valor
    
    public static void main(String[] args) {
        
        int [] myArray = { 12,13,8,45,10, -2 };

        int min = myArray[0];
        int max = myArray[0];

        //System.out.println(min);

        for (int i = 0; i < myArray.length; i++) {
            if (min > myArray[i]) {

                min = myArray[i];
            }
        }

        System.out.println(min);

        for (int i = 0; i < myArray.length; i++) {
            if (max < myArray[i]) {
                
                max = myArray[i];
            }
        }

        System.out.println(max);

    }

}
