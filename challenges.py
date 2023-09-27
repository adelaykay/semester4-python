# Codewriting
# Task 1 of 4
# Given an integer n and an array a of length n, your task is to apply the following mutation to a:

# Array a mutates into a new array b of length n.
# For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
# Example
# For n = 5 and a = [4, 0, 1, -2, 3], the output should be solution(n, a) = [4, 5, -1, 2, 1].

# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
# So, the resulting array after the mutation will be [4, 5, -1, 2, 1].

# Input/Output

# [execution time limit] 4 seconds (js)

# [input] integer n

# An integer representing the length of the given array.

# Guaranteed constraints:
# 1 ≤ n ≤ 103.

# [input] array.integer a

# An array of integers that needs to be mutated.

# Guaranteed constraints:
# a.length = n,
# -103 ≤ a[i] ≤ 103.

# [output] array.integer

# The resulting array after the mutation.


def mutate(n, a):
    '''Mutate a sequence of integers'''
    new_arr = []
    for i in range(n):
        if i == 0:
            new_arr.append(a[i] + a[i + 1])
        elif i >= n - 1:
            new_arr.append(a[i - 1] + a[i])
        else:
            new_arr.append(a[i - 1] + a[i] + a[i + 1])

    return new_arr


lst = [4, 0, 1, -2, 3]
print(mutate(len(lst), lst))

# Task 2 of 4
# Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many ways exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the removal. Note that we are removing only a single instance of a single digit, rather than all instances (eg: removing 1 from the string a11b1c could result in a1b1c or a11bc, but not abc).

# Also note that digits are considered lexicographically smaller than letters.

# Example

# For s = "ab12c" and t = "1zz456", the output should be solution(s, t) = 1.

# Here are all the possible removals:

# We can remove the first digit from s, obtaining "ab2c". "ab2c" > "1zz456", so we don't count this removal
# We can remove the second digit from s, obtaining "ab1c". "ab1c" > "1zz456", so we don't count this removal
# We can remove the first digit from t, obtaining "zz456". "ab12c" < "zz456", so we count this removal
# We can remove the second digit from t, obtaining "1zz56". "ab12c" > "1zz56", so we don't count this removal
# We can remove the third digit from t, obtaining "1zz46". "ab12c" > "1zz46", so we don't count this removal
# We can remove the fourth digit from t, obtaining "1zz45". "ab12c" > "1zz45", so we don't count this removal
# The only valid case where s < t after removing a digit is "ab12c" < "zz456". Therefore, the answer is 1.

# For s = "ab12c" and t = "ab24z", the output should be solution(s, t) = 3.

# There are 4 possible ways of removing the digit:

# "ab1c" < "ab24z"
# "ab2c" > "ab24z"
# "ab12c" < "ab4z"
# "ab12c" < "ab2z"
# Three of these cases match the requirement that s < t, so the answer is 3.

# Input/Output

# [execution time limit] 4 seconds (js)

# [input] string s

# A string consisting of lowercase English letters and digits 0..9.

# Guaranteed constraints:
# 1 ≤ s.length ≤ 103.

# [input] string t

# A string consisting of lowercase English letters and digits 0..9.

# Guaranteed constraints:
# 1 ≤ t.length ≤ 103.

# [output] integer

# The number of ways to remove exactly one digit from one of the strings so that s is lexicographically smaller than t after the removal.


def lexicotract(s, t):
    """calculate how many ways exactly one digit could be removed from one of the strings 
    so that s is lexicographically smaller than t after the removal"""
    count, lst_s, lst_t = 0, list(s), list(t)
    for i, num in enumerate(s):
        if 48 <= ord(num) <= 57:
            lst_s.remove(num)
            count += (''.join(lst_s) < t)
            lst_s.insert(i, num)
    for i, num in enumerate(t):
        if 48 <= ord(num) <= 57:
            lst_t.remove(num)
            count += (''.join(lst_t) > s)
            lst_t.insert(i, num)
    return count


print(lexicotract('ab12c', 'ab24z'))

# Task 4 of 4
# Given an array of integers a of even length, your task is to split it into 
# two arrays of equal length such that all the numbers are unique in each of them.

# There may be more than one possible answer, in which case you may return any of them. 
# If there are no possible answers, return an empty array.

# Hint: Count the number of occurrences of each integer in a. 
# If there are integers occurring more than twice, then there is no solution. 
# Next, put the integers occurring twice into both answer arrays. 
# Finally, put all other numbers in the answer arrays, following the condition 
# that they should have equal sizes.

# Example

# For a = [2, 1, 2, 3, 3, 4], the output can be solution(a) = [[2, 1, 3], [2, 3, 4]].

# Answers like [[1, 2, 3], [2, 3, 4]] or [[4, 2, 3], [3, 2, 1]] would also be considered correct.

# For a = [1, 2, 2, 1], the output can be solution(a) = [[1, 2], [2, 1]].

# Again, there are other possible answers.

# For a = [2, 2, 3, 3, 2, 2], the output should be solution(a) = [].

# No matter how we try to split this array, there will be at least two 2s in at 
# least one of the resulting arrays. So the answer is [].

# Input/Output

# [execution time limit] 4 seconds (js)

# [input] array.integer a

# An array of integers. It is guaranteed that a has even length.

# Guaranteed constraints:
# 2 ≤ a.length ≤ 104,
# 1 ≤ a[i] ≤ 105.

# [output] array.array.integer

# Return an empty array if there is no solution. If a solution exists, 
# return an array of two arrays - a distribution of a where each of these two arrays are of equal length
# and each contains unique elements.


def unique_splt(*nums):
    """Split an array of numbers into two arrays of the same length containing unique elements"""
    solution = [[], []]
    for num in nums:
        if num not in solution[0] and len(solution[0]) < len(nums) / 2:
            solution[0].append(num)
        elif num not in solution[1] and len(solution[1]) < len(nums) / 2:
            solution[1].append(num)
        else:
            return []
    return solution


print(unique_splt(2, 2, 3, 3, 2, 2))


########################################################################
########################################################################
# matriix = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]


# def solution(a):
#     """ Rotate a 2 dimensional array of numbers by 90 degrees clockwise """
#     a.reverse()
#     for i in range(len(a)):
#         for j in range(i):
#             a[i][j], a[j][i] = a[j][i], a[i][j]

#     print(a)


# solution(matriix)


grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]


def solution(grid):
    for i, list_of_nums in enumerate(grid):
        for j, num in enumerate(list_of_nums):
            if ord(num) > 46 and list_of_nums.count(num) > 1:
                print(num)


print(solution(grid))
