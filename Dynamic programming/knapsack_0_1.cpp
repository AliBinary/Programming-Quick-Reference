#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to solve the 0/1 Knapsack problem
int knapsack(const vector<int> &value, const vector<int> &weight, int capacity)
{
    int n = value.size();
    // Create a DP table with dimensions (n+1) x (capacity+1)
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    // Fill the DP table
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 0; j <= capacity; ++j)
        {
            if (j < weight[i - 1])
            {
                dp[i][j] = dp[i - 1][j]; // Item i can't fit in the bag
            }
            else
            {
                dp[i][j] = max(dp[i - 1][j], value[i - 1] + dp[i - 1][j - weight[i - 1]]);
            }
        }
    }

    // The maximum value is stored in dp[n][capacity]
    return dp[n][capacity];
}

int main()
{
    // Example input
    vector<int> value = {80, 24, 23, 22, 21};
    vector<int> weight = {80, 25, 25, 25, 25};
    int capacity = 100;

    // Solve the knapsack problem
    int max_value = knapsack(value, weight, capacity);

    // Output the result
    cout << "Maximum value in Knapsack: " << max_value << endl;

    return 0;
}
