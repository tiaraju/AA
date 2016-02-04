#include <stdio.h>
#include <string.h>


int main(){

	int n,m,repeated;
	
	while (scanf("%d %d",&n, &m) != EOF)
	{
		int i;
		for(i=n;i<=m;i++){
			if(check_repeated(i) == 0){
				repeated++;
			}
		}
		printf("%d\n", (repeated));	
		repeated=0;
	}
	
	return 0;
}


int check_repeated(int i)
{
	char digit[10];
	memset(digit, 0, 10);
	int d = i%10;
	while (i){
		if(digit[d])
		{
			return 1;
		}
		digit[d]=1;
		i/=10;
		d=i%10;
	}
	return 0;
}