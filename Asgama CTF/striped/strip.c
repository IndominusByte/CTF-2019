#include <stdio.h>

int main(){
  int v2,v3,i;
  v2 = 1;
  v3 = 0;
  char a1[20] = "AAAAAAAAAAAAAAAAAAAA";
  
  for(i = 0; i<= 19; i++){
    if(i % 5) 
      v3 += a1[i];
    else 
      v2 *= a1[i];
  }
  printf("result %d\n",v2-v3);
  printf("a1 %s\n",a1);
  printf("a1 index 0 %d",a1[0]);
}
