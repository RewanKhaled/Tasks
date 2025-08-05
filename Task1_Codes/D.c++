#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

//function to calculate the absolute difference between the sums of the matrix's diagonals
int diagonalDifference(vector<vector<int>> arr) {
    int n = arr.size();     //square matrix's size
    int primary = 0;        //primary diagonal's sum
    int secondary = 0;      //secondary diagonal's sum

    for (int i = 0; i < n; ++i) {
        primary += arr[i][i];             // Add primary diagonal element
        secondary += arr[i][n - 1 - i];   // Add secondary diagonal element
    }
    return abs(primary - secondary); //return the absolute difference
}

int main() {
    int n;
    cout << "Enter the size of the square matrix: ";
    cin >> n;
    vector<vector<int>> arr(n, vector<int>(n));
    cout << "Enter the matrix elements:" << endl; // Input matrix elements

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> arr[i][j];

    cout << "Absolute diagonal difference: " << diagonalDifference(arr) << endl;
    return 0;
}
