import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        boolean exit = false;
        Scanner scanner = new Scanner(System.in);
        while (!exit) {
            System.out.println("1. Kalkulator");
            System.out.println("2. Avslutt");
            String choice = scanner.nextLine();
            if(choice.equals("1")) {
                calculator.RunCalculator();
            } else if (choice.equals("2")) {
                exit = true;
            } else {
                System.out.println("ugyldig valg.");
            }
        }
    }
}