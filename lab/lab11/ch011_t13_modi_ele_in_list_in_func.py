def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
    return x

# Example usage:
n = [3, 5, 7]
print(double_list(n))  # Output: [6, 10, 14]