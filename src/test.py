# random_string = "Where are you"
# print(random_string.find("re"))  # First instance of 'is' occurs at index 2
# print(random_string.find("is", 9, 13))  # No instance of 'is' in this range
#
# a_string = "Welcome to Educative!"
# new_string = a_string.replace("Welcome to", "Greetings from")
# print(a_string)
# print(new_string)
#
# num_list = [0, 1, 2, 3, 4, 5]
#
# double_list = map(lambda n: n * 2, num_list)
#
# print(list(double_list))
#
#
# class Calculate:
#     def compute(op, a: int, b: int):
#         print(op(a, b))
#
#
# def fib(n):
#     if n <= 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# def first_and_last(num):
#     last = num % 10
#
#     first = num
#     while first >= 10:
#         first //= 10
#         print(first)
#
#     print("first", first, "last", last)
#     return first + last
#
#
# def check_balance(brackets):  # The argument is a string
#     open_count = 0
#
#     for char in brackets:
#         if char == "]":
#             if open_count == 0:
#                 return False
#             else:
#                 open_count -= 1
#         else:
#             open_count += 1
#
#     return open_count == 0
#

def detect_pattern(s1, s2):
    # this function takes two parameters as strings to compare.
    # Keep in mind that this method should return the same value
    # no matter what order the two strings are passed

    if len(s1) != len(s2):
        return False

    for index in range(len(s1)):

        s1_index=index_of( s1[index],s1,index+1)
        s2_index=index_of( s2[index],s2,index+1)

        if s1_index!=s2_index:
                return False

    return True

def index_of(val, in_list,index):
    try:
        return in_list.index(val,index)
    except ValueError:
        return -1



if __name__ == "__main__":
    # For nested lists
    populations = [["Winterfell", 10000], ["King's Landing", 50000],
                   ["Iron Islands", 5000], ["King's Landing", 50000]]
    print(populations)
    populations.remove(["King's Landing", 50000])
    print(populations[1:2])
