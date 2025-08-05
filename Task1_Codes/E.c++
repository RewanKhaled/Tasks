#include <iostream>
#include <vector>
using namespace std;

// Function to count apples and oranges that land on the house
void countApplesAndOranges(int s, int t, int a, int b, vector<int> apples, vector<int> oranges) {
    int appleCount = 0, orangeCount = 0;

    // Count how many apples fall on the house
    for (int d : apples) {
        int landingPos = a + d; // Final position of the apple
        if (landingPos >= s && landingPos <= t)
            appleCount++;
    }

    // Count how many oranges fall on the house
    for (int d : oranges) {
        int landingPos = b + d; // Final position of the orange
        if (landingPos >= s && landingPos <= t)
            orangeCount++;
    }

    // Output the results
    cout << "Apples on the house: " << appleCount << endl;
    cout << "Oranges on the house: " << orangeCount << endl;
}

int main() {
    int s, t; // start and end point of the house
    int a, b; // position of the apple and orange trees
    int m, n; // number of apples and oranges

    cout << "Enter start and end point of the house: ";
    cin >> s >> t;

    cout << "Enter position of apple tree and orange tree: ";
    cin >> a >> b;

    cout << "Enter number of apples and oranges: ";
    cin >> m >> n;

    vector<int> apples(m), oranges(n);

    cout << "Enter distances at which each apple falls from the tree: ";
    for (int i = 0; i < m; ++i)
        cin >> apples[i];

    cout << "Enter distances at which each orange falls from the tree: ";
    for (int i = 0; i < n; ++i)
        cin >> oranges[i];

    countApplesAndOranges(s, t, a, b, apples, oranges);
    return 0;
}