#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int angle;
	cin >> angle;
	int total =0;
	for(int i=1;i<=60;i++)
	{
		if(total == angle)
		{
			cout << 'Y'<<endl;
			return 0;
		}
		if(i%12 != 0 )
		{
			total+=6;
		}
	}
	cout << 'N'<<endl;
	return 0;
}