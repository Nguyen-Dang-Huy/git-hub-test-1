#include <cmath>
#include <iostream>
#include <string>
using namespace std;
/******************************************************************************
 * Support Functions: these functions below are optional. If you want your code
					  to be clearer, you can implement them. However if you
					  dont know how to use funtion in programming, dont worry, 
					  you dont have to implement them, and you just add a comment 
					  in each of them.
*******************************************************************************/
int move(string moves)
{   
	int i,x=0,y=0,dis;
	for (i=0;i<=moves.length()-1;i++)
	{
		if (moves[i]=='U')
			y=y+moves[i+1]*1-48;
		if (moves[i]=='D')
			y=y-(moves[i+1]*1-48);
		if (moves[i]=='R')
			x=x+moves[i+1]*1-48;
		if (moves[i]=='L')
			x=x-(moves[i+1]*1-48);
	}
	return round(sqrt(x*x+y*y));
}

bool isPrime(int n)
{
    int i,dem=0;
	if (n==2)
		return true;
	else
	{
		for (i=1;i<=n;i++)
		{
			if (n%i==0)
			{
				dem=dem+1;
			}
		}
		if (dem==2)
			return true;
		else
			return false;
	}
}

bool isSquared(int n)
{
    int i,k,d;
	d=0;
	k=round(sqrt(n));
	for (i=0;i<=k;i++)
		{
			if (i*i==n)
			{
				d=1;
				break;
			}
		}
	if (d==1)
		return true;
	else
		return false;
}

int main()
{
    string moves;
    int distance;
    bool primality, squared;

    /// =======================================================
    /*
        The following code initializes variable `moves`
    */
    /// BEGIN   TESTCASE
    cin >> moves;
    /// END     TESTCASE

    /*---------------------------------
        * Calculate the distance
        * Remember to assign calculated value to variable `distance`
	*/
    /*TODO: add your code here*/
    
    
	distance=move(moves);
    /*---------------------------------*/
    cout << "Khoang cach xe da di chuyen tu vi tri ban dau toi diem hien tai: "
        << distance << '\n';


    /*---------------------------------
        * Check if distance is prime
        * Remember to assign appropriate value to variable `primality`
	*/
    /*TODO: add your code here*/
    primality=isPrime(distance);
	squared=isSquared(distance);
    

    /*---------------------------------*/

    /*---------------------------------
        * Check if distance is squared
        * Remember to assign appropriate value to variable `squared`
	*/
    /*TODO: add your code here*/

    

    /*---------------------------------*/

    if (primality) {
        cout << "So " << distance << " la so nguyen to\n";
    }
    if (squared) {
        cout << "So " << distance << " la so chinh phuong\n";
    }

    return 0;
}