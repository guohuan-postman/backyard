import os
import yaml

def read_yaml_file(method,whichtime):
    current_path = os.path.abspath(os.path.dirname(__file__))
    print(current_path)
    print(current_path + 'qingjia_riqi.yaml')
    with open(current_path + '\qingjia_riqi.yaml', 'r', encoding='utf-8') as f:
        fi = f.read()
        temp = yaml.load(fi, Loader=yaml.FullLoader)
        print(temp)
        print(temp[method][whichtime])
        return temp[method][whichtime]

if __name__ == '__main__':
    ti = read_yaml_file('chanjianjia9day_fail', 'startTime')
    print('shijian')
    print(ti)
