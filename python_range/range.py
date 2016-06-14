# _*_ coding: utf-8 _*_
import random
def generate_verification_code(len=6):
    '''随机生成六位的验证码'''
    #注意:这里我们生成的是0-9A-Za-z的列表,当然你也可已制定这个list,这里很灵活
    #比如:code_list = ['P','y','t','h','o','n','T','a','b'] #PythonTab的字母

    code_list = []
    for i in range(10): #0-9数字
        code_list.append(str(i))
    for i in range(65,91): #对应"A"到"Z"的ASCII码
        code_list.append(chr(i))
    for i in range(97,123): #对应"a"到"z"的ASCII码
        code_list.append(chr(i))
    myslice = random.sample(code_list,len) #从list中随机抽取6个元素,作为一个片段返回
    verification_code = ''.join(myslice) #list to string
    return verification_code

code = generate_verification_code(6)
print code