#include <stdio.h>

int main(void){
    char siblings[3][20] = {"Alex", "Mara", "Madi"};
    int i;
    for(i=0;i<3;i++){
        printf("%s\n", siblings[i]);
    }
    
    return 0;
}
    