#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

int main(){
	int n,c,d,result;
	cin >> n;

	for (int i = 0; i < n; ++i)
	{
		cin >>c>>d;
		if(c==0 && d==0)
		{
			cout<<0<<endl;
		}
		else
		{
			result =pow(26,c)*pow(10,d);
			printf("%d\n",result);
		}
	}
}
