#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int num,originalNum,rem,result=0;
	cout<<"enter the number: ";
	cin>>num;
	originalNum=num;
	while(originalNum!=0)
	{
		rem = originalNum % 10;
		result = result + pow(rem,3);
        originalNum /= 10;		
	}
	if (result == num)
        cout << num << " is an Armstrong number.";
    else
        cout << num << " is not an Armstrong number.";

    return 0;
	
}
