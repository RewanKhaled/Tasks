#include <iostream>
#include <algorithm>

int main() {
    long long k2, k3, k5, k6;  // variables to store the counts of digits 2, 3, 5, and 6
    std::cout << "Enter the number of 2s, 3s, 5s, and 6s: "; //input the counts of the digits
    std::cin >> k2 >> k3 >> k5 >> k6;

    long long count256 = std::min({k2, k5, k6}); // calculate how many 256 numbers can be formed using one 2, one 5, and one 6
    k2 -= count256;  // subtract the used 2s to form 256 so we can reuse remaining 2s for 32
    long long count32 = std::min(k2, k3);  //calculate how many 32 numbers can be formed using one 2 and one 3
    long long result = count256 * 256 + count32 * 32; //calculate the total result: 256 * count256 + 32 * count32

    std::cout << "Maximum total sum using 256 and 32 numbers: " << result << std::endl;
    return 0;
}