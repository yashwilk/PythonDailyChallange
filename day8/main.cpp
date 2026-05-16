#include<iostream>
using namespace std;

int main(){
    double principle,rate,time;
    cout<<"Enter Principle";
    cin>>principle;
    cout<<"Enter rate%";
    cin>>rate;
    cout<<"Enter Time";
    cin>>time;
    double si=(principle*rate*time)/100;
    cout<<"Simple Interest: "<<si<<endl;
    return 0;
}
