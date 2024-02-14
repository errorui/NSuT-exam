def variable_argument(*args):
    for i in args:
        print(i)


variable_argument('a', 'b', 'c', 'd')       