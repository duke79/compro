T = input()

tweets = dict()


def print_output():
    ret = 0
    for key, value in tweets.items():
        if value:
            ret += 1
    print(ret)


for i in range(int(T)):
    ret = "regularly fancy"
    try:
        quote = input()
        for word in quote.split(" "):
            if word == "not":
                ret = "Real Fancy"
                break
    except ValueError as e:
        pass
    print(ret)
