#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int n,k;
	cin >>n>>k;

	for ( int i =0;i<n;i++)
	{
		if(i>0)
		{
			cout << " ";
		}
		if(k>0)
		{
			cout << 2*i+2<<" "<<2*i+1;
		}
		else
		{
			cout << 2*i+1<<" "<<2*i+2;
		}
		k--;
	}
	return 0;
}