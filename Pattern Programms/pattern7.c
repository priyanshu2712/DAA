#include<stdio.h>
/*
    * * * * *   |       1 2 3 4 5   |       A B C D E
   * * * * *    |      1 2 3 4 5    |      A B C D E
  * * * * *     |     1 2 3 4 5     |     A B C D E
 * * * * *      |    1 2 3 4 5      |    A B C D E
* * * * *       |   1 2 3 4 5       |   A B C D E
*/
int main()
{
    for(int i=0; i<= 4; i++)
    {
        for(int j=4; j>=i; j--)
        {
            printf(" ");
        }
        for(int k=0; k<=4; k++)
        {printf("*");}
        printf("\n");
    }
}