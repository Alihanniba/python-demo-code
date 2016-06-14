# _*_ coding: utf-8 _*_
import random


def generate_verification_code_v2():
    code_list = []
    for i in range(2):
        random_num = random.randint(0, 9)  # 随机生成0-9的数字
        # 利用random.randint()函数生成一个随机整数a,使得65<=a<=90
        # 对应从"A"到"Z"的ASCII码
        a = random.randint(65, 90)
        b = random.randint(97, 122)
        random_uppercase_letter = chr(a)
        random_lowercase_letter = chr(b)
        code_list.append(str(random_num))
        code_list.append(str(random_uppercase_letter))
        code_list.append(str(random_lowercase_letter))
    verification = ''.join(code_list)
    return verification


code = generate_verification_code_v2()
