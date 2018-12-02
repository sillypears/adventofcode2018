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
    count = 0
    two = 0
    three = 0
    for id in data:
        letters = {}
        foundtwo = False
        foundthree = False
        for letter in id:
            if letters.get(letter):
                letters[letter] += 1
            else:
                letters[letter] = 1
        for letter in sorted(letters):
            if letters[letter] == 2 and foundtwo == False:
                #print("Found 2 {}'s: {}".format(letter, id))
                foundtwo = True
                two += 1
            if letters[letter] == 3 and foundthree == False:
                #print("Found 3 {}'s: {}".format(letter, id))
                foundthree = True
                three += 1
        count += 1
    print("2: {}, 3: {}".format(two, three))
    print("Checksum: {}".format(two * three))

if __name__ == "__main__":
    sys.exit(main())