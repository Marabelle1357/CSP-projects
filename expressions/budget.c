#include <stdio.h>

int main(void){
    float income, rent, utilities, groceries, transportation, expenses, savings, total;
    float prent, putilities, pgroceries, ptranspotation, pexpenses;
    printf("This code is going to calculate your bugdet for the month. ");
    printf("How much do you make in a month?:\n");
    scanf("%f", &income);
    printf("How much do you pay in rent per month?:\n");
    scanf("%f", &rent);
    printf("How much do you pay in utilities per month?:\n");
    scanf("%f", &utilities);
    printf("How much do you pay in groceries per month?:\n");
    scanf("%f", &groceries);
    printf("How much do you pay in transportation in a month?:\n");
    scanf("%f", &transportation);
    expenses = rent + utilities + groceries + transportation;
    savings = income*.2;
    total = income-expenses-savings;
    prent = rent/income;
    putilities = utilities/income;
    pgroceries = groceries/income;
    ptranspotation = transportation/income;
    pexpenses = expenses/income;
    printf("Your income is: $%.2f\n", income);
    printf("Your expenses are: $%.2f\n", expenses);
    printf("Your savings are: $%.2f\n", savings);
    printf("Your total left to spend is: $%.2f\n", total);
    printf("Your rent payment is: %.2f", prent, "of your expenses");
    printf("Your utilities payment is: %.2f", putilities, "of your expenses");
    printf("Your groceries payment is: %.2f", pgroceries, "of your expenses");
    printf("Your transportation payment is: %.2f", ptranspotation, "of your expenses");
    return 0;
}