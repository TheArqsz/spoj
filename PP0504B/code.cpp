#include <iostream>
#include <cstring>
 
using namespace std;
 
#define T_SIZE 1001
 
char* string_merge(char *, char *);
 
int main(){
	int t,n;
	char S1[T_SIZE], S2[T_SIZE], *S;
 
	cin >> t; /* wczytaj liczbę testów */
	cin.getline(S1,T_SIZE);
 
	while(t){
		cin.getline(S1,T_SIZE,' ');
		cin.getline(S2,T_SIZE);
 
		S=string_merge(S1,S2);
		cout << S << endl;
		delete[] S;
		t--;
	}
 
	return 0;
}
 
char* string_merge(char* s1, char* s2) {

    char* merged = (char *)malloc((T_SIZE * 2 - 1) * sizeof(char));

    int j = 0;

    for(int i = 0; i < T_SIZE; i++) {

        if(s1[i] == '\0' || s2[i] == '\0') {
            break;
        }

        merged[j] = s1[i];
        j++;

        merged[j] = s2[i];
        j++;

    }
    merged[j] = '\0';

    return merged;

}