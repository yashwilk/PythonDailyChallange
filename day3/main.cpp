"""Question: Find the Second Largest Element in an Array"""
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int secondLargest(vector<int>& arr) {
    int largest = INT_MIN;
    int second = INT_MIN;

    for (int num : arr) {
        if (num > largest) {
            second = largest;
            largest = num;
        }
        else if (num > second && num != largest) {
            second = num;
        }
    }

    return second;
}

int main(){
    vector<int> arr={3, 1, 4, 1, 5, 9};
    cout <<secondLargest(arr) ;
    return 0;       
}