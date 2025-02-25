import java.text.NumberFormat;
import java.util.Scanner;

public class Calculator {
    private int principal;
    private float annualInterest;
    private float monthlyInterest;
    private final byte MonthsInYear = 12;
    private final byte Percent = 100;
    private Scanner scanner = new Scanner(System.in);
    private int numberOfPayments;
    public void RunCalculator() {
        loanamount();
        interest();
        years();
        monthlyCost();
    }

    private void monthlyCost() {
        double mortgage = principal
                * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);
        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Lånekostnad (mnd): " + mortgageFormatted);
        System.out.println();
    }

    private void years() {
        System.out.print("Periode (år): ");
        while (true) {
            byte years = scanner.nextByte();
            if(years < 1 || years > 30) {
                System.out.println("Periode skal være mellom 1 og 30 år");
            } else {
                numberOfPayments = years * MonthsInYear;
                break;
            }
        }
    }

    private void interest() {
        System.out.print("Rente: ");
        while (true) {
            annualInterest = scanner.nextFloat();
            if(annualInterest < 1 || annualInterest > 15) {
                System.out.println("Rente skal være mellom 1 og 15");
            } else {
                monthlyInterest = annualInterest / Percent / MonthsInYear;
                break;
            }
        }
    }

    private void loanamount() {
        System.out.print("Lånesum (10000 - 10000000): ");
        while (true) {
            principal = scanner.nextInt();
            if (principal < 10000 || principal > 10000000) {
                System.out.println("Lånesum må være mellom 10000 og 10000000");
            } else {
                break;
            }
        }
    }
}
