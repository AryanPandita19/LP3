#include <iostream>
#include <vector>
#include <algorithm>

int knapsack_0_1(std::vector<int>& values, std::vector<int>& weights, int capacity) {
    int n = values.size();
    std::vector<int> dp(capacity + 1, 0);

    for (int i = 0; i < n; i++) {
        for (int w = capacity; w >= weights[i]; w--) {
            dp[w] = std::max(dp[w], values[i] + dp[w - weights[i]]);
        }
    }

    return dp[capacity];
}

int main() {
    int n, capacity;
    std::cin >> n;
    std::vector<int> values(n), weights(n);

    for (int i = 0; i < n; ++i)
        std::cin >> values[i] >> weights[i];

    std::cin >> capacity;
    int max_value = knapsack_0_1(values, weights, capacity);

    std::cout << "Maximum value: " << max_value << std::endl;

    return 0;
}
