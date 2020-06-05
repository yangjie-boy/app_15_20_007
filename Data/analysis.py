import yaml

with open("./search.yml", "r", encoding="utf-8")as f:
    # 解析yaml文件
    data_list = []
    data = yaml.safe_load(f)
    # print(data.values())
    for i in data.values():
        data_list.append((i.get("input"), i.get("exp")))
    print(data_list)
