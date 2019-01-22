#include <stdio.h>
#include<string.h> 

int lenk;
char k[32];
int main(int argc,char* argv[]){
 char* s;
 int i;
 s = strdup(argv[0]);
 lenk = strlen(s) - 2;

 printf("lenk : %d\n",lenk);
 printf("strdup : %s\n",s);

 for ( i = 0; i < strlen(s); ++i )
    k[i] = s[i + 2];

 printf("isi k %s",k);
}
