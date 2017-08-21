#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	int add = 1; //add increments to get the next natural number
	int check = 1; //number of divisors
    	int num;
    	for (long i = 0; i < 99999999;) //"i" is the number we're looking for.
	{
		i+=add;
		//cout << (i) << endl; //testing accuracy of generation of new triangle numbers.
		num = (int) sqrt(i); //to increase efficiency, check only upto the square root of number. 
		for (int j = 1; j <= num; j++)
		{
			if (i % j == 0)
			{
				//cout << j << " is a divisor of " << i << endl;
				check+=2;
				if (j*j == num) //check for square roots, subtract 1 because "double" solution
					check--;
			}
		}
		check-=1; //Subtract 1 to account for extra "check" in the 'j loop'.
      
		cout << "Triangle number #" << add << " : " << i << endl;
		//cout << "# of divisors: " << check << " of " << i << endl; //testing program

		if (check >= 500) //check to see if there are 500 or more divisors for this particular 'i'. 
		{
			cout << "Final answer: " << i << endl
				i = 99999999;
		}
		
		check = 1; //reset the divisor check for the next iteration (i.e. 'i' value).
		add++; //increment to get help get the next triangle number.
	}
}
