import threading
import random

with open("hamlet.txt") as f:
    hamlet = " ".join([line.strip() for line in f.readlines()]).lower()

CHARSET = []
threads = []
lucky_chimps = 0

for char in hamlet:
    if char not in CHARSET:
        CHARSET.append(char)
CHARSET.sort()

letters_to_match = int(input("How many letters to match in Hamlet? [Enter 0 to match entire text] "))
if letters_to_match:
    excerpt = hamlet[:letters_to_match]
else:
    excerpt = hamlet

print(f"Text to match (case insensitive): '{excerpt}'")


def spawn_chimp(num_letters):  # Optimized, still slow as fuck
    global lucky_chimps
    idx = 0
    while idx < letters_to_match:
        randlet = random.choice(CHARSET)
        if randlet != excerpt[idx]:
            return
        idx += 1
    if idx == letters_to_match:
        lucky_chimps += 1


num_of_chimps = int(input("How many monkeys to simulate? "))


for i in range(num_of_chimps):
    t = threading.Thread(target=spawn_chimp, args=(letters_to_match,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()


if lucky_chimps:
    print(f"{lucky_chimps} out of your {num_of_chimps} chimps recreated Hamlet! ({round(lucky_chimps / num_of_chimps, 7) * 100}%)")
else:
    print(f"Your {num_of_chimps} chimps could not recreate Hamlet!")
