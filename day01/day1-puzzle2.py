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
    #data = get_test_input()
    sum = 0
    count = 0
    seen = {}
    seen["0"] = 1
    mybreak = True
    while (mybreak):
        for item in data:
            #print("{} + {} = {}".format(item, str(sum), str(int(item)+sum)))
            sum += int(item)
            count += 1
            if (seen.get(str(sum))):
                seen[str(sum)] += 1
            else:
                seen[str(sum)] = 1
            #print("{}, {}, {}, {}".format(count, item, sum, seen[str(sum)]))

            if seen[str(sum)] == 2:
                print("{} seen twice in {} loops".format(sum, count/len(data)))
                mybreak = False
                break

if __name__ == "__main__":
    sys.exit(main())