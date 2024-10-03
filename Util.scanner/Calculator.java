import java.util.Scanner;

class calculator {

    public static void main(String[] args) {
        
        char operator;
        Double number1, number2, result;

        Scanner input = new Scanner(System.in);

        System.out.println("Elige un operador: +, -, * or /");

        operator = input.next().charAt(0);

        System.out.println("Ingresa un número");
        number1 = input.nextDouble();

        System.out.println("Ingresa un número");
        number2 = input.nextDouble();

        switch (operator) {
            case '+':
                result = number1 + number2;
                System.out.println("El resultado es: "+result);
                break;
        
            case '-':
                result = number1 - number2;
                System.out.println("El resultado es: "+result);
                break;

            case '*':
                result = number1 * number2;
                System.out.println("El resultado es: "+result);
                break; 
                
            case '/':
                result = number1 / number2;
                System.out.println("El resultado es: "+result);
                break;    

            default:
            System.out.println("Operador inválido!");
                break;
        }

        input.close();

    }

}

