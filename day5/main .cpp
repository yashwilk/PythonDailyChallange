"""Question: Find the Missing Number in an Array"""
"""Input:
[3,0,1]

Output:
2"""

#include,iostream>
#include<vector>

using namespace std;


int missingnumber(vector<int>& nums){
    int n=nums.size()
    expectedsum=n*(n+1)/2
    int actualsum=0
    for (int num: nums){
    actualsum+=num;
    }
    return expectedSum - actualSum;
}


int main(){
    vector<int> nums={0,1,3};
cout<< missingnumber(nums);
return0;
}