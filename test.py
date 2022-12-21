#coding:utf-8
# import pyyaml module
import yaml
from yaml.loader import SafeLoader

def validDictParam(p: dict, p1: dict) -> bool:
    '''
    参数p:期望值,p1:实际值

    类型p: dict, p1:dict
    '''
    # 初始化验证通过
    vaild = True
    for key, value in p.items():
        if key not in p1.keys() or value != p1[key]:
            vaild = False
            break

    return vaild


def vaildListParam(p: list, p1: list, key: str) -> bool:
    '''
    参数p:期望值,p1:实际值,key:数据主键

    类型p: list, p1:list, key:str
    '''
    vaild = True
    vaildCount = 0
    for item in p:
        item_dict = dict(item)
        key_value = item_dict[key] #主键值
        for p1_item in p1:
            if isinstance(p1_item, dict):
                p1_dict = dict(p1_item)
                if key in p1_dict.keys() and p1_dict[key] == key_value:
                    result = validDictParam(item_dict, p1_dict)
                    if not result:
                        vaild = False
                        break
                    else:
                       vaildCount +=1 #验证成功条数+1

    return vaild and vaildCount == len(p)


with open('text.yml', encoding='utf-8') as f:
    data = yaml.load(f, Loader=SafeLoader)
    for item in data:
        # 事件
        e = dict(item['e'])

        # 写入kafka

        # 第三方入参
        if isinstance(item['p'], list):
            key = item['key']
            p_list = list(item['p'])
            p = [{'id1' : 123, 'name1' : "jjj"}, {'id1' : 456, 'name1' : "jjjk"}]
            result = vaildListParam(p_list, p, key)
            print(result)            
        
        if isinstance(item['p'], dict):
            p = dict(item['p'])
            p1 = {  'id' : 123, 'name1' : "jjj", 'x': "x1" }   # 实际参数
            result = validDictParam(p, p1)
            print(result)
            
        # 第三方返回值
        r = dict(item['r'])


