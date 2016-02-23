#include <stdio.h>

int MIN(a,b)
{
	return (a<b)?a:b;	
} 

int main()
{
	int n,m;
	scanf("%d %d",&n,&m);

	int diagonal = MIN(n,m);
	int possible = diagonal+1;
	printf("%d\n",possible);
	int i;
	for(i=0;i<possible;i++)
	{
		printf("%d %d\n",i,(diagonal-i));
	}

	return 0;
	
}


