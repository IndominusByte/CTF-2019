#include <stdio.h>

int main(int argc,char* argv[]){
  char *v3; // rbp@2
  signed int v4; // ebx@2
  int v6; // r9@4
  char v7; // cl@5
  int v8; // edi@5
  int v9; // rsi@6
  int v10; // rcx@6
  int v11; // eax@7

if ( argc <= 1 )
  {
    v4 = 1;
    __printf_chk(1LL, "%s <flag>\n", argv[0]);
  }
/*
  else
  {
    v3 = argv[1];
    v4 = 1;
    if ( strlen(argv[1]) == 20 )
    {
      v6 = 0LL;
      do
      {
        v7 = v3[v6];
        v8 = 0;
        do
        {
          v9 = v7;
          v10 = v8++;
          v7 = *(&byte_201040[256 * v10] + v9);
        }
        while ( v8 != 20 );
        v11 = byte_201020[v6++] == v7;
        v4 &= v11;
      }
      while ( v6 != 20 );
      if ( v4 )
        __printf_chk(1LL, "Arkav5{%s}\n", v3);
      v4 ^= 1u;
    }
  }
  return v4;
  */
}
