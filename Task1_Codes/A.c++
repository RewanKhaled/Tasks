#include <iostream>
#include <vector>
#include <iomanip>

int main() {
    int n;
    std::cout << "Enter the number of elements: "; // user entering the number of elements
    std::cin >> n;
    std::vector<int> p(n);
    double sum = 0.0;

    std::cout << "Enter " << n << " integers:" << std::endl; // read elements and calculate the sum
    for (int i = 0; i < n; ++i) {
        std::cin >> p[i];
        sum += p[i];
    }
    // calculate the average
    double result = sum / n;

    // display the result with high precision
    std::cout << "The average is: ";
    std::cout << std::fixed << std::setprecision(12) << result << std::endl;
    return 0;
}
