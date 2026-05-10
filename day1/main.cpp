#include<isotream>
#include<vector>

using namespace std;

vector<double> movingAverage(vector<int>& price,int k) """why amersand """
vector<double> result;
double windowSum=0;
for(int i=0;i<price.size();i++)
windowsum+=price[i];
if(i>=k){
    windowSum-=price[i-k];
}
if(i>=k-1)
    result.push_back(windowSum/k);
return result;

int main(){
    vector<int> price={1,2,3,4,5,6};
    int k =3;
    vector<double> ans = movingAverage(price, k);
    for(double val:ans){
        cout<<val<<" ";
    }
}