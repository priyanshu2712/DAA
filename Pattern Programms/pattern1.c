#include<stdio.h>
/* 
*
**
***
****
*****
*/
int main()
{
    for(int i=0; i<6; i++)
    {
        for(int j=0;j<i;j++){ /* here j<i and not j<6 because if j<6 everytime the line is 5 *  
        so it should be less than 6
        */
        printf("*");}
        printf("\n");
    }

}