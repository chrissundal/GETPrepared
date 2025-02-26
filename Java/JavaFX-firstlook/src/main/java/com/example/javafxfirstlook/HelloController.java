package com.example.javafxfirstlook;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;

public class HelloController {
    @FXML
    private TextField debtField;

    @FXML
    private TextField incomeField;

    @FXML
    private TextField principalField;

    @FXML
    private TextField interestField;

    @FXML
    private TextField yearsField;

    @FXML
    private Label errorLabel;

    @FXML
    private Label resultLabel1;

    @FXML
    private Label resultLabel2;

    @FXML
    private Label resultLabel3;

    @FXML
    private Label resultLabel4;

    @FXML
    private VBox vboxInputs;

    @FXML
    private VBox vboxResults;


    @FXML
    void resetCalculator() {
        vboxInputs.setVisible(true);
        vboxResults.setVisible(false);
    }

    @FXML
    void calculateMortgage() {
        try {
            int principal = Integer.parseInt(principalField.getText());
            float annualInterest = Float.parseFloat(interestField.getText().replace(",", "."));
            int years = Integer.parseInt(yearsField.getText());
            int income = Integer.parseInt(incomeField.getText());
            int debt = Integer.parseInt(debtField.getText());

            if (typingChecks(principal, annualInterest, years)) return;

            Calculator calculator = new Calculator(principal, annualInterest, years, income, debt);
            double mortgage = calculator.calculateMonthlyCost();
            double maxLoan = calculator.CalculateMaxLoan();
            if(maxLoan < principal) {
                vboxInputs.setVisible(false);
                vboxResults.setVisible(true);
                resultLabel1.setText("Du har ikke råd til dette lånet");
                resultLabel2.setText("Maksimalt lån: " + String.format("%.2f", maxLoan) + " kr " + "basert på din inntekt: " + income + " kr.");
                resultLabel3.setText("Du ba om: " + principal + " kr " + "og har: " + debt + " kr i gjeld.");
            } else {
                vboxInputs.setVisible(false);
                vboxResults.setVisible(true);
                double percentOfincome = calculator.CalculateCanPay();
                if (percentOfincome < 40) {
                    double monthlyIncome = income / 12;
                    double leftOver = monthlyIncome - mortgage;
                    resultLabel1.setText("Dine kostnader er på " + String.format("%.2f",percentOfincome) + "% av din inntekt.");
                    resultLabel2.setText("Du har " + monthlyIncome + " kr i månedlig inntekt basert på din årlige inntekt: " + income + " kr.");
                    resultLabel3.setText("Lånekostnad (mnd): " + String.format("%.2f", mortgage) + " kr ");
                    resultLabel4.setText("Du vil ha " + String.format("%.2f",leftOver) + " kr å leve for i måneden.");
                } else {
                    resultLabel1.setText("Du har god nok inntekt, men månedlige kostnader overstiger 40%");
                    resultLabel2.setText("Dine kostnader vil være på " + String.format("%.2f",percentOfincome) + "% av din inntekt.");
                    resultLabel3.setText("Vennligst prøv igjen");
                    resultLabel4.setText("");
                }
            }
        } catch (NumberFormatException e) {
            errorLabel.setText("Vennligst skriv inn gyldige tall.");
        }
    }

    private boolean typingChecks(int principal, float annualInterest, int years) {

        if (principal < 10000 || principal > 10000000) {
            errorLabel.setText("Lånesum må være mellom 10000 og 10000000");
            return true;
        }
        if (annualInterest < 1 || annualInterest > 15) {
            errorLabel.setText("Rente skal være mellom 1 og 15");
            return true;
        }
        if (years < 1 || years > 30) {
            errorLabel.setText("Periode skal være mellom 1 og 30 år");
            return true;
        }
        return false;
    }
}
