#include<iostream>
using namespace std;
 
int maxSubArraySum(int a[], int size)
{
    int pos = 0,max_so_far = 0,l = 0, max_ending_here = 0;
 
    for (int i = 0; i < size; i++)
    {
        max_ending_here = max_ending_here + a[i];
        pos += a[i];
        if (max_ending_here < 0 && l == 0)
    	 	{
    	 	max_ending_here -= a[i];
    	 	pos = 0;
    	 	l = 1;
            # max_ending_here = 0;
    	 	}
    	if (max_ending_here < 0 && l == 1)
    	 	{
    	 	l = 0;
            max_ending_here = pos;
            max_ending_here -= a[i];
            pos = 0;
            if(max_ending_here < 0)
            	max_ending_here = 0;
    	 	}
        if (max_so_far < max_ending_here)
            max_so_far = max_ending_here;
    }
    return max_so_far;
}
int main()
	{
		int t;cin>>t;
		while(t--){
		int n;cin>>n;
		int a[n+1];
		for(int i=0;i<n;i++){
			cin>>a[i];
		}
		int ans = maxSubArraySum(a,n);
		cout<<ans;
		}
	}




















