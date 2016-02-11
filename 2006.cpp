#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int n,t;
	int total =0;
	cin >> n;

	for(int i=0;i<5;i++)
	{
		cin >> t;
		if(t == n)
		{
			total++;
		}
	}
	cout << total << endl;
	return 0;
}