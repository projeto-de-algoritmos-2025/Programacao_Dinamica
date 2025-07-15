int trap(int *height, int n) {
    if (n < 3) return 0;
    int *leftMax  = malloc(n * sizeof(int));
    int *rightMax = malloc(n * sizeof(int));
    leftMax[0] = height[0];
    for (int i = 1; i < n; ++i) {
        if (height[i] > leftMax[i - 1]) {
            leftMax[i] = height[i];
        } else {
            leftMax[i] = leftMax[i - 1];
        }
    }
    rightMax[n - 1] = height[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        if (height[i] > rightMax[i + 1]) {
            rightMax[i] = height[i];
        } else {
            rightMax[i] = rightMax[i + 1];
        }
    }
    int water = 0;
    for (int i = 1; i < n - 1; ++i) {
        int minLR;
        if (leftMax[i] < rightMax[i]) {
            minLR = leftMax[i];
        } else {
            minLR = rightMax[i];
        }
        if (minLR > height[i]) {
            water += minLR - height[i];
        }
    }
    return water;
}
