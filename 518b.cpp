#include <stdio.h>
#include <string.h>
#include <iostream>
#include <map>

using namespace std;
char reverse(char c);

int main ()
{
	string s, t;
	cin >> s >> t;
	map<char,int> qnt;

	for (int i = 0; i < t.length(); i++)
		qnt[t[i]]++;

	int ans1 = 0, ans2 = 0;
	for (int i = 0; i < s.length(); i++)
	{
		if (qnt[s[i]] > 0)
		{
			qnt[s[i]]--;
			ans1++;
			s[i] = 0;
		}
		else 
		{
			s[i] = reverse(s[i]);
		}
	}

	for (int i = 0; i < s.length(); i++)
	{
		if (qnt[s[i]] > 0)
		{
			qnt[s[i]]--;
			ans2++;
			s[i] = 0;
		}
	}

	cout << ans1 << " " << ans2 << endl;
}

char reverse(char ch)
{
	if ('a' <= ch && ch <= 'z') 
        return ch = ch - 'a' + 'A';
    else
        return ch = ch - 'A' + 'a';
}