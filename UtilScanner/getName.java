import java.util.Scanner;

/**
 * getName
 */
class getName {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        System.out.println("Ingresa tu nombre :");

        String name = input.nextLine();

        System.out.println("Mi nombre es "+ name);

        input.close();
    }
    
}