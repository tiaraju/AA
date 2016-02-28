#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;
int main(){

	int n,menor,total;
	cin >> n;
	string s;

	for(int i=0;i<n;i++){
		cin >> s;
		menor =0;
		total =0;
		for(int k=0;k<s.length();k++){
			if(s[k] == '<'){
				menor++;
			}else if (s[k]=='>' && menor>0){
				total++;
				menor--;
			}
		}
		cout << total << endl;
	}
}