"""Check if a String is a Palindrome"""
#include<iostream>
#include<string>
using namespace std;

bool ispalindrome(string s){
    int left=0;
    int right =s.size()-1;
    while(left<right){
        if(s[left]!=s[right]){
            return false;
    }
    left++;
    right--;

}
return true;
}

intmain(){
    string s="madam";
    if(ispalindrome(s))
        cout<<s<<" is a palindrome."<<endl;
    else
        cout<<s<<" is not a palindrome."<<endl;
    return 0;  
    
}