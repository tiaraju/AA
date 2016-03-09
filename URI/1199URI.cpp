#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string>

using namespace std;

int convert(char str[])
{
	int number;
	if(str[1]=='x')
	{
		number = atoi(str[2]);
	}
	else
	{
		number = stoi(str);
	}

	return number;
}


int main()
{
	int i;
	string str;
	cin >> str;
	i = convert(str);
	while(i>0)
	{
		if(str[1]=='x')
		{
			cout << "0x"<<i<<endl;
		}
		else
		{
			cout << i << endl;
		}
		cin >> str;
		i = convert(str);
	}
}
