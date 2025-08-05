#include <iostream>
using namespace std;

int main() {
    int t;
    cout << "Enter the number of test cases: "; //entering the number of test cases
    cin >> t;

    // Loop through each test case
    while (t--) {
        int n;
        cout << "Enter a number: "; //entering the value for this test case
        cin >> n;
        cout << "Half of the number is: " << n / 2 << endl; // Output half of the number using integer division
    }
    return 0;
}
