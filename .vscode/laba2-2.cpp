#include <iostream>

auto square(auto x) {
    return x * x;
}

int main() {
    std::cout << square(5) << std::endl;
    std::cout << square(2.5) << std::endl;

    return 0;
}