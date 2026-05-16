#include<isostream>
using namespace std;
int main(){
    cout,,"Hello World";
    return 0;

}


#include<isostream>
using namespace std;
int main(){
    double a,b;
    cout<<"Enter two numbers";
    cin>>a>>b;
    cout<<"The Sum is: "<<a+b<<endl;
    return 0;
}

#include<isostream>
using namespace std;
int main(){
double celsius;
cout<<"Enter temperature in Celsius: ";
cin>>celsius;
double fahrenheit=(celsius*9/5)+32;
cout<<celsius<<"-C"<<fahrenheit<<"-F"<<endl;
return 0;
}


#include<isostream>
#include<vector>
using namespace std;
int maxprofit(vector<int>& prices){
    int minprice=price[0];
    int maxprofit=0;
    for (int price: prices){
        minprice=min(minprice, price);
        int profit=price-minprice;
        maxprofit=max(maxprofit, profit);
        return maxprofit;
    }
int main(){
    vector<int> prices={7,1,5,3,6,4};
    cout<<maxprofit(prices);
    return 0;   
}
