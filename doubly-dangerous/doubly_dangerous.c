//compile with:
//gcc -m32 -std=c99 -Wall -fno-stack-protector doubly_dangerous.c -o doubly_dangerous

//sol: input "A"*40+"\x00\x80\x34\x41"

#define _GNU_SOURCE
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>

void give_flag() {
    FILE *f = fopen("flag.txt", "r");
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    if (f != NULL) {
        char c;

        while ((c = fgetc(f)) != EOF) {
            putchar(c);
        }
        fclose(f);
    }
    else {
        printf("Failed to open flag file!\n");
    }
}

int main(int argc, char **argv){
  volatile float modified;
  char buffer[64];

  modified = 0;
  printf("Give me a string: \n");
  gets(buffer);

  if (modified == 11.28125) {
      printf("Success! Here is your flag:\n");
      give_flag();
  } 
  else {
      printf("nope!\n");
  }
}
