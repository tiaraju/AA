#include <stdio.h>


int main(){
	
	int n;
	scanf("%d",&n);
	int numbers[n];

	int firstPart=0;
	int secondPart=0;
	int total=0;

	int i,k;
	for(i=0;i<n;i++)
	{
		scanf("%d",&numbers[i]);
		secondPart+=numbers[i];
	}

	for(i=0;i<n-1;i++)
	{
		firstPart+=numbers[i];
		secondPart-=numbers[i];
		if(firstPart == secondPart)
		{
			total++;
		}
		
	}
	printf("%d\n",total);
	return 0;
}