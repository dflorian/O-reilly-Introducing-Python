#! python3
# 11.1
import zoo
zoo.hours()

# 11.2
import zoo as menagerie
menagerie.hours()

# 11.3
from zoo import hours
hours()

# 11.4
from zoo import hours as info
info()

# 11.5
from pprint import pprint

plain = {'a':1, 'b':2, 'c':3}
pprint(plain)

# 11.6
from collections import OrderedDict
fancy = OrderedDict(plain)

pprint(fancy)

# 11.7
from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists)

# palindrome
def palindrome(word):
	return word == word[::-1]

print(palindrome("test"))
print(palindrome("radar"))