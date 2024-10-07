package ArraysExercises;

import java.util.Arrays;

public class Exercise1 {

    public static void main(String[] args) {
        
        int [] myArray1 = {
            1789, 2035, 1899, 1456, 2013,
            1458, 2458, 1254, 1472, 2365,
            1456, 2165, 1457, 2456
        };

        String [] myArray2 = {
            "Java", "Janko", "Jennifer",
            "mamá", "papá", "hijo"
        };

        System.out.println(Arrays.toString(myArray1));
        System.out.println(myArray1);

        System.out.println(myArray2);
        System.out.println(Arrays.toString(myArray2));

    }
}