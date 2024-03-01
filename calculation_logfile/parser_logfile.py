import re

res = {}
# Для каждой строки лога ищем совпадение с помощью re. Делаем две группы: с IP и кб. 
with open("ip.log") as file:
    for line in file.readlines():
        match = re.search(r"^(\S+) - \S+ - (\d+)", line)
 # суммируем количество кб для каждого IP, используя словарь res, где ключ IP, а значение суммарное кб.
        res[match.group(1)] = res.get(match.group(1), 0) + int(match.group(2))
# выводим IP и общее количество кб, которые были переданы с этого IP адреса.
for ip, s in res.items():
    print(ip + " : " + str(s))
