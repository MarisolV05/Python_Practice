
#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max ([a,b,c])

print(max_num(1,2,3))
print(max_num(15,30,2))
print(max_num(1000,50,1))

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
    if len(list) == 0:
        return 0
    prod = list[0]

    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i
    return prod

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))

#Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    return string[::-1]

print(rev_string(""))
print(rev_string("apple"))
print(rev_string("banana"))

#Write a Python function called num_within() to check whether a number falls in a given range
def num_within(number, start_range, end_range):
    return start_range <= number <= end_range

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    if n <= 0:
        print("Number of rows should be a positive integer.")
        return

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
        row.append(1)
        triangle.append(row)
 # code to make the triangle
    for row in triangle:
        print(' '.join(map(str, row)).center(n*3))

pascal(5)