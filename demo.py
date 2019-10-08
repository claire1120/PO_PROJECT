
import yaml
# data = {'Search_Data': {
# 						'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
# 						'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
# with open("./text.yaml","w",encoding="utf-8") as f:
#     # 在当前目录下生成text.yaml文件，若文件存在直接更新内容
# 	yaml.dump(data,f,encoding="utf-8", allow_unicode = True)
def main():
    with open("./data.yml", 'r', encoding="utf-8" ) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(type(data))  # 打印data类型
        print(data)  # 打印data返回值

if __name__ == '__main__':
    main()