#include <stdio.h>

int main()
{

	int a,c;
	int block[c];
	scanf("%d %d",&a,&c);
	while(a != 0 && c!=0)
	{
		int i;
		int resposta=0;
		for(i=0;i<c;i++)
		{
			scanf("%d",&block[i]);
		}

		for(i=0;i<c;i++)
		{
			if(i==0)
			{
				if(block[i]<a)
				{
					resposta+=(a-block[i]);
				}
			}
			else
			{
				if(block[i] < block[i-1])
				{
					resposta+=(block[i-1]-block[i]);
				}
			}
		}
		printf("%d\n",resposta);
		scanf("%d %d",&a,&c);
	}
	return 0;
}