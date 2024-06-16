def levenshtein(source, target):
    m = len(source)
    n = len(target)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m + 1):
        for j in range(n + 1):
            # source = #, target = #you
            if i == 0:
                dp[i][j] = j
            # source = #yu, target = #
            elif j == 0:
                dp[i][j] = i
            elif source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[m][n]


print(levenshtein('yu', 'you'))
