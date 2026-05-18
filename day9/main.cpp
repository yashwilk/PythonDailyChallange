#include <iostream>
#include <vector>
#include <cmath>


using namespace std;


double volatility(vector<double>& returns){

    double mean=0;

    for(double r: returns){
        mean+=r;        
    }
            mean/=returns.size();
    double variance=0;

    for(double r: returns){
             variance += pow(r - mean, 2);
    } 
    return sqrt(variance / returns.size());
}


int main() {

    vector<double> returns = {
        0.01, -0.02, 0.015, 0.03
    };

    cout << volatility(returns);

    return 0;
}