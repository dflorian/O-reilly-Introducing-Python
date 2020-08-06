#! python3
# 8.1
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)

# 8.2
print(e2f["walrus"])

# 8.3
f2e = {}
for english, french in e2f.items():
	f2e[french] = english

print(f2e)

# 8.4
print(f2e["chien"])

# 8.5
print(f2e.values())

# 8.6
life = {
	"animals": {"cats":["Henri", "Grumpy", "Lucy"], "octopi":{}, "emus":{}},
	"plants": {},
	"other": {},
}

print(life)

# 8.7
print(life.keys())

# 8.8
print(life['animals'].keys())

# 8.9
print(life['animals']['cats'])

# 8.10
square = {i: i **2 for i in range(10)}

# 8.11
odd = {i for i in range(10) if i%2 == 1}
print(odd)

#8.12
print([('Got '+str(i)) for i in range(10)])

#8.13
key = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
print(zip(key, values))

#8.14
titles = ['Creatures of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
print(zip(titles, plots))