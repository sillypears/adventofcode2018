import requests, os, sys

AUTH=""

def get_inputs(day):
    url = "https://adventofcode.com/2018/day/{}/input".format(day)
    cookies = dict(session=AUTH)
    r = requests.get(url, cookies=cookies)
    if r.status_code == 200:
        return r.text.splitlines()
    else:
        print("Couldn't get inputs, update cookie")
        sys.exit(1)

def get_test_inputs():
    with open('test_input.txt', 'r') as f:
        return f.read().splitlines()

def main():
    data = get_inputs("2")
    #data = get_test_inputs()
    for id in data:
        good_letters = []
        for compare in data:
            good_letters = []
            if id is not compare:
                for i in range(0, len(id)):
                    if id[i] == compare[i]:
                        good_letters.append(id[i])
            if len(id) - len(good_letters) == 1:
                print("Output is: {}".format(''.join(good_letters)))
                sys.exit()

if __name__ == "__main__":
    sys.exit(main())