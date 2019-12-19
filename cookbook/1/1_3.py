# 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # yield line, previous_lines
            previous_lines.append(line)
    # print(previous_lines)
    return previous_lines
# Example use on a file
if __name__ == '__main__':
    with open(r'test.txt') as f:
        test = search(f, 'python', 7)
        print(test)
        # for line, prevlines in search(f, 'python', 5):
        #     print(prevlines)
            # print(line, end='')

