public class Account {

    private String accountNumber;
    private double balance;

    public Account(String accountNumber, double balance){
        if (accountNumber == null || accountNumber.isEmpty()) {
            System.err.println("El número de cuenta no puede ser nulo o vacío");
            return;
        }
        if (balance < 0) {
            System.err.println("el balance no puede ser menor a cero");
            return;
        }

        this.accountNumber = accountNumber;
        this.balance=balance;
    }

    public static void main(String[] args) {
        
        Account account1 = new Account("123456", 5);

        System.out.println(account1.accountNumber+" "+account1.balance);
    }
}

