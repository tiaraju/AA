#include <stdio.h>

int main()
{
	int n;
	float d,a,b;
	float coef_a,coef_b;

	scanf("%d",&n);
	scanf("%f %f %f",&d,&a,&b);

	
	coef_a=a/d;
	coef_b=b/d;

	int i;
	for(i=0;i<=n;i++)
	{
		scanf("%f %f %f",&d,&a,&b);
		if(coef_a>b/d || coef_b<a/d)
		{
			printf("N\n");
			return 0; 
		}
		else
		{
			if(a/d > coef_a)
			{
				coef_a = a/d;
			}

			if(b/d < coef_b)
			{
				coef_b=b/d;
			}
		}
	}

	printf("Y\n");
	return 0;
}