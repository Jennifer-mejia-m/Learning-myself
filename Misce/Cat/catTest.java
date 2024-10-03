package Cat;

public class catTest {

    public static void main(String[] args) {
        
        cat jimeno = new cat();

        cat man = new cat("Jankito",3);

        System.out.println(jimeno.getName());
        System.out.println(jimeno.getAge());

        System.out.println(man.getName());
        System.out.println(man.getAge());

        jimeno.setName("burito");

        System.out.println(jimeno.getName());
        
    }
    
}
