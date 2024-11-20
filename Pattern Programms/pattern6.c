#include<stdio.h>
/* * * * * * * * * *  |   1 2 3 4 5 6 7 8 9   |   A B C D E F G H I
    * * * * * * *     |     1 2 3 4 5 6 7     |     A B C D E F G
      * * * * *       |       1 2 3 4 5       |       A B C D E
       * * *          |         1 2 3          |         A B C
         *            |           1            |           A        */
int main()
{
    for(int i=0; i<=5; i++)
    {
        for(int j=0; j<=i; j++)
        printf(" ");
        for(int k=5; k>=i; k-- )
       { printf(" *");}

        printf("\n");
    }
}