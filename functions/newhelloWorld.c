#include <stdio.h>


void names(char name[]){
printf("Hello %s",name);
}


int main(void){
    names("Starli(oldest parent)\n");
    names("Mike(youngest parent)\n");
    names("Alex(youngest child)\n");
    names("Mara(middle child)\n");
    names("Madi(youngest child)");
    return 0;
}