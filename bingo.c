#include <stdio.h>
#include <math.h>

int balls[90];

int main(){

	int n,b;
	scanf("%d",&n);
	scanf("%d",&b);

	while(n!= 0 || b!=0){
		int i,k,j;
		for(i=0;i<b;i++){
			scanf("%d",&balls[i]);
		}

		int contains[n];
		
		for(i=0;i<=n;i++){
			contains[i]=0;
		}

		for(i=0;i<=n;i++){
			for(k=0;k<b;k++){
				for(j=k;j<b;j++){
					if(abs(balls[j]-balls[k]) == i){
						contains[i]=1;
						break;
					}
				}
			}
		}
		int possible=1;
		for(i=0;i<=n;i++){
			if(contains[i]==0){
				possible=0;
				break;
			}
		}

		if(possible == 0 ){
			printf("N\n");
		}else{
			printf("Y\n");
		}

		scanf("%d",&n);
		scanf("%d",&b);

	}


	return 0;
}