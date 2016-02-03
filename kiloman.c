#include <stdio.h>

int shots[50];
char position[50];

int main(){
	int n,s;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++){
		scanf("%d",&s);
		int k;
		int hit=0;
		for(k=0;k<s;k++){
			scanf("%d",&shots[k]);
		}
		for(k=0;k<s;k++){
			scanf(" %c",&position[k]);
		}

		for(k=0;k<s;k++){
			if(position[k]=='J'){
				if(shots[k]>2){
					hit++;
				}
			}else{
				if(shots[k]<=2 & shots[k]>0){
					hit++;
				}

			}
		}
		printf("%d\n",hit);
	}
	return 0;
}