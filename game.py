import json
import random


people = ['도둑', '경찰', '평민', '의사']
suspect = ("%s" % random.choice(people))

with open('test.txt', 'w', encoding='utf-8') as f:
    json.dump(suspect, f, ensure_ascii = False)
with open('test.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    result = json.loads(data)
print(result)

