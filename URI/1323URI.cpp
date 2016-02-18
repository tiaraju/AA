#include <stdio.h>
#include <iostream>
using namespace std;
int how_many_squares(int n);
int main()
{
	int n;
	cin >> n;
	while(n != 0 )
	{
		cout << how_many_squares(n) << endl;
		cin >> n;
	}
	return 0;
}
int how_many_squares(int n)
{
	return (n*(n+1)*(2*n+1))/6;
}
