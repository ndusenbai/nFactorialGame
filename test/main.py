import time
import json
def done_json():
    new_value = 7
    file = {1: 10, 2: 15, 3: 20, 4: 2, 5: 7, 6: 45, 7: 21, 8: 31, 9: 22, 10: 38}
    done_json = {}

    value_list = list(file.values())
    value_list.append(new_value)
    value_list = sorted(value_list)

    for value in range(10):
        done_json[value] = value_list[value]

    print(done_json)

if __name__ == '__main__':
    with open('test.json', 'r') as f:
        #data = f.read()
        data = json.load(f)
        print(data)
