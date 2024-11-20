#include<stdio.h>
int main()
{
    for(int i=0; i<=4; i++)
    {
        for(int j=4; j>=i; j--) // 4 3 2 1 0 for i = 0;  for i = 1: 4 3 2 1 ;
        {
            printf(" ");
        }
        for(int k=0; k<=i  ;k++)
        {
            printf("* ");
        }
        printf("\n");
    }
}