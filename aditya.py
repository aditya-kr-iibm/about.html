totalmarks = int(input("enter total marks"))
if totalmarks >= 700 and totalmarks <= 900:
    print("A++ Grade")
elif totalmarks >= 600 and totalmarks <= 699:
    print("A+ Grade")
elif totalmarks <= 500 and totalmarks <= 599:
    print("A Grade")
elif totalmarks <= 400 and totalmarks <= 499:
    print("B Grade")
elif totalmarks <= 300 and totalmarks <= 399:
    print("C Grade")
elif totalmarks <= 200 and totalmarks <= 299:
    print("D Grade")
else:
    print("fail")