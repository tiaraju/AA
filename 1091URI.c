#include <stdio.h>


int main()
{
	int k,m,n,x,y;

	while(scanf("%d %d %d",&k,&x,&y) != EOF){

		int i;
		for(i=0;i<k;i++){
			scanf("%d %d",&n,&m);

			if(n == x || m == y)
			{
				printf("divisa\n");
			}
			else if(n > x && m > y)
			{
				printf("NE\n");
			}
			else if(n> x && m<y)
			{
				printf("SE\n");
			}
			else if(n < x && m<y)
			{
				printf("SO\n");
			}
			else if(n < x && m>y)
			{
				printf("NO\n");
			}
		}
	}

	return 0;
}