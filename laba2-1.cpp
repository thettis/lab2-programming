// #include <iostream>
// #include <string>
// int main(){
//     std::string name = "Рената";
//     std::string date = "08.10.26";

//     std::cout << "Hello world" << std::endl;
//     std::cout <<name << std::endl;
//     std::cout << date << std::endl;
//     return 0;
// }

// #include <iostream>

// auto square(auto x) {
//     return x * x;
// }

// int main() {
//     std::cout << square(5) << std::endl;
//     std::cout << square(2.5) << std::endl;

//     return 0;
// }

#include <iostream>
int factorial(int n) {
  if (n <= 1)
    return 1;
  return n * factorial(n - 1);
}
int main() {
  std::cout << factorial(5) << std::endl;
  return 0;
}