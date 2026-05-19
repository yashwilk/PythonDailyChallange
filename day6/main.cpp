// Compute Running Average of Stock Prices
#include <iostream>
using namespace std;

class RunningAverage {
private:
    double sum;
    int count;
public:
    RunningAverage() {
        sum = 0;
        count = 0;
    }
    double next(int price) {
        sum += price;
        count++;
        return sum / count;
    }
};

int main() {
    RunningAverage avg;
    cout << avg.next(100) << endl;
    return 0;
}




#Write a C++ function to calculate the moving average of stock prices over a window size k.
#include <iostream>
#include <vector>

using namespace std;
vector<double> movingAverage(vector<int>& prices, int k){
    vector<double> result;
    double windowSum=0;
    for(int i=0,i<price.saize(),i++({
        windowsum+=price[i];
        if(i>=k-1){
            result.push_back(windowSum/k);
            windowSum-=price[i-k+1];
        }
    }
    return result;
}

int main() {
    vector<int> prices = {1, 2, 3, 4, 5};
    int k = 3;

    vector<double> ans = movingAverage(prices, k);

    for (double val : ans) {
        cout << val << " ";
    }

    return 0;
}