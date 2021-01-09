#include <iostream>
using namespace std;

int main()
{
    int n,num,rev=0,digit;
    cout<<"enter number: ";
    cin>>num;
    n=num;
    while(num!=0)
    {
    	digit = num % 10;                  
        rev = (rev * 10) + digit;
        num = num / 10;
	}
	cout << " The reverse of the number is: " << rev << endl;  // reverse of number

     if (n == rev)
         cout << " The number is a palindrome.";
     else
         cout << " The number is not a palindrome.";

    return 0;
}
