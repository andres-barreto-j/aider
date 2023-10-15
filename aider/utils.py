from pathlib import Path

from .dump import dump  # noqa: F401


def safe_abs_path(res):
    "Gives an abs path, which safely returns a full (not 8.3) windows path"
    res = Path(res).resolve()
    return str(res)


def show_messages(messages, title=None, functions=None):
    if title:
        print(title.upper(), "*" * 50)

    for msg in messages:
        role = msg["role"].upper()
        content = msg.get("content")
        if content:
            for line in content.splitlines():
                print(role, line)
        content = msg.get("function_call")
        if content:
            print(role, content)

    if functions:
        dump(functions)


def word_distance_v1(word1, word2):
    """
    Calculates the minimum number of operations (insertion, deletion, or replacement) required to transform word1 into word2.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        int: The minimum number of operations required to transform word1 into word2.
    """
    def helper(i, j):
        if i == 0:
            return j  # Insert all characters from word2
        if j == 0:
            return i  # Delete all characters from word1

        if word1[i - 1] == word2[j - 1]:
            return helper(i - 1, j - 1)
        else:
            insert = 1 + helper(i, j - 1)      # Insert a character
            delete = 1 + helper(i - 1, j)      # Delete a character
            replace = 1 + helper(i - 1, j - 1)  # Replace a character
            return min(insert, delete, replace)

    output = helper(len(word1), len(word2))

    print(f'Para {word1}, {word2}=> {output}')
    
    return output


def word_distance(word1, word2):
    m, n = len(word1), len(word2)

    # Create a matrix to store the distances between substrings of word1 and word2.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the matrix.
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the matrix using dynamic programming.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]

