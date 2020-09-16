import os

import main


def test():
    copy_paths = './sim_0.8'
    origin_path = './orig.txt'
    ans_path='./answer.TXT'
    for path in os.listdir(copy_paths):
        print(f'{path}:', main.get_similar(f'{copy_paths}/{path}', origin_path))
        # res = os.system(f'python main.py {origin_path} {copy_paths}/{path} {ans_path}')
        # print(f'{path}:',res)
        # print(f'{path}一样:', main.get_similar(origin_path, origin_path))
    # # 参数缺失
    res = os.system(f'python main.py {origin_path}')
    print(res)
    #
    # # 无效文本
    res = os.system(f'python main.py {origin_path} ./empty.txt ./answer.TXT')
    print(res)
    #
    # # 文件不存在
    res = os.system(f'python main.py ./0000.txt ./empty.txt ./answer.TXT')
    print(res)

#文章一样

if __name__ == '__main__':
    test()