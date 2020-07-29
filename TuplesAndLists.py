#! python3
# 7.1
year_list = [year for year in range(1990,2020)]
print(year_list)

#7.2
thirdBday = year_list[3]

#7.3
oldest = year_list[-1]

#7.4
things = ["mozarella", "cinderella", "salmonella"]

#7.5
things = [thing.capitalize() if thing == "cinderella" else thing for thing in things]	
print(things)

#7.6
things = [thing.upper() if thing == "mozarella" else thing for thing in things]	
print(things)

#7.7
things.pop()
print(things)

#7.8
surprise = ["Grupo", "Chico", "Harpo"]

#7.9
print(surprise[-1].lower()[::-1].upper())

#7.10
even = [number for number in range(10) if number%2 ==0]

#7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
	("flop", "get a mop"),
	("fope", "turn the rope"),
	("fa", "get your ma"),
	("fudge", "call the judge"),
	("fat", "pet the cat"),
	("fog", "walk the dog"),
	("fun", "say we're done")
]
start2 = "Someone better"

for (first, second) in rhymes:
	print("! ".join(start1).upper() + "! " + first.upper())
	print(start2 + " " + second + ".")