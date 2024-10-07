package ArraysExercises;

public class Exercise4 {

    public static boolean contains(int [] myArray, int item) {
        for (int n : myArray) {
            if (item==n) {
                return true;
            } 
            }
            return false;
        }
    
    
    public static void main(String[] args) {
        
        int [] myArray1 = {
            1789, 2035, 1899, 1456, 2013,
            4568, 1990
        };

        System.out.println(contains(myArray1, 1991));

        System.out.println(contains(myArray1, 1456));

    }
}
