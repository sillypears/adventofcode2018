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
    data = get_inputs("1")
    #data = get_test_inputs()
    sum = 0
    for item in data:
        sum += int(item)
    print(sum)

if __name__ == "__main__":
    sys.exit(main())