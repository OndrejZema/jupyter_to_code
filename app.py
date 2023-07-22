import json
import sys
import os
def main(file_path):
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print('Bad file path')
        return
    
    source_code = []

    with open(file_path, mode="r", encoding="utf-8") as source:
        data = json.load(source)
        for i in data["cells"]:
            if i['cell_type'] == "code":
                source_code.extend(i["source"])
    
    with open(file_path.replace(file_path.split('.')[-1], '.py'), mode='w', encoding='utf-8') as output:
        output.write(''.join(source_code))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Expected 1 argument")
        exit()

    
    main(sys.argv[1])
