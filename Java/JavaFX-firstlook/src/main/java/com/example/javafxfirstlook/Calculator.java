package com.example.javafxfirstlook;

public class Calculator {
    private int principal;
    private float annualInterest;
    private float monthlyInterest;
    private final byte MonthsInYear = 12;
    private final byte Percent = 100;
    private int numberOfPayments;
    private int income;
    private int loans;

    public Calculator(int principal, float annualInterest, int years,int income, int loans) {
        this.principal = principal;
        this.annualInterest = annualInterest;
        this.monthlyInterest = annualInterest / Percent / MonthsInYear;
        this.numberOfPayments = years * MonthsInYear;
        this.income = income;
        this.loans = loans;
    }

    public double calculateMonthlyCost() {
        double mortgage = principal
                * (monthlyInterest * Math.pow(1 + monthlyInterest, numberOfPayments))
                / (Math.pow(1 + monthlyInterest, numberOfPayments) - 1);
        return mortgage;
    }
    public double CalculateMaxLoan() {
        double maxLoan = income * 5;
        double sum = maxLoan - loans;
        return sum;
    }

    public double CalculateCanPay() {
        double monthlyIncome = income / MonthsInYear;
        double monthlyMortgage = calculateMonthlyCost();
        double percentageOfIncome = (monthlyMortgage / monthlyIncome) * 100;
        return percentageOfIncome;
    }
}

