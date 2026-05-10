"""Question: Check if a Number is Prime"""

#include<iostream>
using namespace std;

bool isprime(int n){
    if(n<=1)
        return false;
    for (int i=2;i*i<=n;i++){
        if(n%i==0)
            return false;
    }
    return true;
}


int main(){
    int n=29;

    if(isprime(n)){
        cout<<n<<" is a prime number."<<endl;
    }else{
        cout<<n<<" is not a prime number."<<endl;
    }
    return 0;
}