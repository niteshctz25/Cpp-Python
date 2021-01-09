
#include <iostream>
using namespace std;
int main()
{
    char input, alphabet = 'A';
    int i, j;
 
    cout << "Enter the uppercase character you want to print in the last row:";
    cin >> input;
    for(int i = 1; i <= (input-'A'+1); i++)
    {
        for(int j = 1; j <= i; j++)
        {
            cout << alphabet << " ";
        }
        alphabet++;
        cout << "\n";
    }
    return 0;
}
