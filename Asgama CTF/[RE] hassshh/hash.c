#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main(){
  int v1,v2 = 0,v4,result;
  char v8[32];
  srand(time(NULL));
  v1 = rand() % 500;

  puts("masukkan kata yang sesuai dengan angka!");
  printf("%d\n",v1);
  printf("input : ");
  scanf("%s",v8);

  v4 = strlen(v8);

  if (v4 <= 1)
    result = 0xFFFFFFFFLL;
  else{
    for ( int i = 0; i < v4 - 1; ++i )
      v2 += v8[i];
    result = v2 * v8[v4 -1];
  }

  printf("lengt input %d\n",v4);
  printf("result : %d\n",result);
}
