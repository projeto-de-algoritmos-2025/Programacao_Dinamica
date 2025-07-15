int maxCoins(int *nums, int n) {
    int m = n + 2;
    int *val = malloc(m * sizeof(int));
    val[0] = val[m - 1] = 1;
    for (int i = 0; i < n; ++i) val[i + 1] = nums[i];
    int *dp = calloc(m * m, sizeof(int));    
    for (int len = 2; len < m; ++len) {
        for (int l = 0; l + len < m; ++l) {
            int r = l + len;
            int best = 0;
            for (int k = l + 1; k < r; ++k) {
                int gain = val[l] * val[k] * val[r] + dp[l * m + k] + dp[k * m + r];
                if (gain > best) best = gain;
            }
            dp[l * m + r] = best;
        }
    }
    return dp[0 * m + (m - 1)];
}
