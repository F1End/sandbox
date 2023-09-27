import logging

from mymodules import mylib1

_logger = logging.getLogger(__name__)

# print("Hello there!")
# _logger.warning("WARNING TEST HERE!")


#arguments

def standard(arg):
    print(arg)

# Not working in Python 3.6 but works in Python 3.11
# def pos_only(arg, /):
#     print(arg)

def kwd_only(*, arg):
    print(arg)

# def combined(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)

standard("Test")
standard(arg="Test2")
# pos_only("Test3")
# pos_only(arg="Test4")
# kwd_only("Test5")
kwd_only(arg="Test6")

# combined("blah", standard="bleh", kwd_only="bloh")

## Positional argument for kwds prevents ambuigity
## Use positional if you want the name to be unavailable for the user

# def foo(name, **kwds):
#     return 'name' in kwds
#
# foo(1, **{'name': 2})

# def foo(name, /, **kwds):
#     return 'name' in kwds

# print(foo(1, **{'name': 2}))

# Not working in Python 3.6 but works in Python 3.11
my_list = [last := x for x in range(0,11)] ## := keeps value after local scope
your_list = [1,2,3,
             4,5,]  #traling comma
print(my_list)
print(last)
print(your_list)


from collections import abc

print(issubclass(list, abc.Sequence))