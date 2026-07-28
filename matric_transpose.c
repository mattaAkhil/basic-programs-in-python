#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<process.h>
void main(){
    int a,b,temp;
    printf("enter row length of the matrix:");
    scanf("%d",&a);
    printf("enter column length of the matrix:");
    scanf("%d",&b);
    int z[a][b];
    for(int i=0;i<a;i++){
        for (int j=0;j<b;j++){
            printf("enter element of index[%d,%d]:",i,j);
            scanf("%d",&z[i][j]);
        }
    }
    printf("the matrix is:\n");
    for(int i=0;i<a;i++){
        for (int j=0;j<b;j++){
            printf("%d",z[i][j]);
        }
        printf("\n");
    }
    printf("transposed matrix:");
    for(int i=0;i<a;i++){
        for (int j=i;j<b;j++){
            temp=z[i][j];
            z[i][j]=z[j][i];
            z[j][i]=temp;
        }
       
    }
for(int i=0;i<a;i++){
        for (int j=0;j<b;j++){
            printf("%d",z[i][j]);
        }
        printf("\n");
    }
}