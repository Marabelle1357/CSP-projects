#include <stdio.h>

int main(void){
    char name[15];
    printf("What is your name?: \n");
    scanf("%s", name);
    char beg = ("###");
    char end = ("###");
    strcat(beg,name);
    strcat(beg,end);
    printf("%s",beg);
    return 0;
}