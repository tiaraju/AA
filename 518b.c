#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int size=2e5 +1;

	char s[size];
	char t[size];
	
	fgets(s,sizeof(s),stdin);
	fgets(t,sizeof(t),stdin);

	

	return 0;
}

int isUpperCase(char c)
{
	if(c >='A' && c<='Z'){
		return 1;
	}
	return 0;
}


char f(char c)
{
		if ('a' <= c && c <= 'z')
			return ch - 'a' + 'A';
		return + 32;
}

