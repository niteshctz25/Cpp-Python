#include <stdio.h>
#include <string.h>
int main()
{
  int c = 0;
  char ch,s[100];
  int length;

  printf("Enter a string \n");
  gets(s);

  length = strlen(s);

  printf("Length of the string = %d\n", length);
  
   while (s[c] != '\0') {
      ch = s[c];
      if (ch >= 'A' && ch <= 'Z')
         s[c] = s[c] + 32;
      else if (ch >= 'a' && ch <= 'z')
         s[c] = s[c] - 32;  
      c++;  
   }
   
   printf("%s\n", s);

  return 0;
}
