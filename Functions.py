#! python3
# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

# 9.2
def get_odds():
    odds = [x for x in range(10) if x % 2 == 0]
    return odds

print (get_odds())

# 9.3
def test(func):
    def new_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_function

@test
def add_ints(a, b):
    print(a+b)
    return a+b

add_ints(2,3)

#9.4
class OopsException(Exception):
    print ('Caught an oops')

try:
    t= 1/0
except:
    raise OopsException()