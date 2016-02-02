#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char reverse(char c);

int main()
{
	int size=2e5 +1;

	char s[size];
	char t[size];
	
	fgets(s,sizeof(s),stdin);
	fgets(t,sizeof(t),stdin);

	int i,k;
	int y=0;
	int w=0;

	for(i=0;i<strlen(s);i++){
		for(k=0;strlen(t);k++){
			if(s[i]==t[k]){
				y++;
				t[k]='-';
				break;
			}else if(s[i]==reverse(t[k])){
				w++;
				t[k]='-';
				break;
			}
		}

	}
	

	printf("%d %d",y,w);

	return 0;
}

char reverse(char c)
{
		if ('a' <= c && c <= 'z')
			return c - 'a' + 'A';
		return c + 32;
}

