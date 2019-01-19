#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int num[10];
int arr[10];

void gen(int a1){
  int v1; // ecx@5
  int v2[48] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,
                 173,179,181,191,193,197,199}; // [sp+10h] [bp-D0h]@1
  int i; // [sp+D0h] [bp-10h]@1
  int v4; // [sp+D4h] [bp-Ch]@2
  int v5; // [sp+D8h] [bp-8h]@2
  int v6; // [sp+DCh] [bp-4h]@2

  srand(a1);
  for ( i = 0; i <= 9; ++i )
  {
    v4 = 0;
    v5 = 0;
    v6 = 164;//148
    num[i] = 164;
    while ( v6 > 1 )
    {
      if ( !(v6 % v2[v4]) )
      {
        v6 /= v2[v4];
        v5 += v2[v4];
        v4 = -1;
      }
      v1 = v4 + 1;
      v4 = (v4 + 1) / 47;
      v4 = v1 - 47 * v4;
    }
    arr[i] = v5;
  }
}
int createseed(){
  int result; // rax@2
  unsigned int buf; // [sp+8h] [bp-8h]@3
  int fd; // [sp+Ch] [bp-4h]@1

  fd = open("/dev/urandom", 0);
  if ( fd == -1 )
  {
    puts("Open error on /dev/urandom!");
    result = 0xFFFFFFFFLL;
  }
  else if ( read(fd, &buf, 4uLL) == 4 )
  {
    result = buf;
  }
  else
  {
    puts("Read error!\n");
    result = 0xFFFFFFFFLL;
  }
  return result;
}
int main(){
  unsigned int v3; // eax@1
  time_t v4; // rax@2
  int v6; // [sp+Ch] [bp-24h]@2
  double v7; // [sp+10h] [bp-20h]@2
  time_t time0; // [sp+18h] [bp-18h]@2
  int i; // [sp+24h] [bp-Ch]@1
  int v10; // [sp+28h] [bp-8h]@1
  int v11; // [sp+2Ch] [bp-4h]@1
  char name[20];

  printf("What's your name? ");
  scanf("%s", name);
  printf("Hi, %s\n", name);
  puts("Given 10 numbers, calculate sum of its prime factors!");
  puts("You have 2 seconds to solve a number :)");
  v3 = createseed();
  gen(v3);
  v10 = 0;
  v11 = 0;
  for ( i = 0; i <= 9; ++i )
  {
    printf("%d : %d\n", (i + 1), num[i]);
    printf("Sum: ");
    time0 = time(0LL);
    scanf("%d", &v6);
    printf("arr %d \n",arr[i]);
    v4 = time(0LL);
    v7 = difftime(v4, time0);
    if ( v7 > 2.0 )
    {
      puts("Time's up!");
      v10 = 1;
      break;
    }
    if ( arr[i] != v6 )
    {
      v10 = 1;
      break;
    }
    ++v11;
  }
  if ( v10 )
  {
    puts("Try again next time...");
  }
  else if ( v11 == 10 )
  {
    printf("Congrats!\nHere's your prize: %p\nCan you give a feedback? ", &name);
  }
  return 0;
}
