#include <algorithm>
#include <iterator>

int arr[] = {1, 3, 5, 7};

void foo() {
    std::transform(std::begin(arr), std::end(arr), std::begin(arr),
                   [](int x) { return x * x; });
}
