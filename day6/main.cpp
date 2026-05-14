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
