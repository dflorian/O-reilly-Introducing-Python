#! python3
# 13.1
from datetime import datetime
now = datetime.now()

f = open("today.txt", "w")
f.write(str(now))
f.close()

#13.2
f = open("today.txt", "r")
today_string = f.read()
print(today_string)

#13.3
parsed = datetime.strptime(today_string, '%Y-%m-%d %H:%M:%S.%f')
print(parsed.date())

#13.4
from datetime import date
bday = date(1990, 8, 30)
sentence = "My birthday is on %B %d, %Y"
print(bday.strftime(sentence))

#13.5
text = "My birthday was on a %A"
print(bday.strftime(text))

#13.6
from datetime import timedelta
older = bday + timedelta(10000)
sentence = "I was 10k days old on %B %d, %Y"
print(older.strftime(sentence))