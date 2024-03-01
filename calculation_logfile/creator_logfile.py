import random
import time

# словарь из 10 ip адресов и связанных с ними доменными именами
ip_dict = {
    "1.1.1.1": "11111.com",
    "2.2.2.2": "22222.com",
    "3.3.3.3": "33333.com",
    "4.4.4.4": "44444.com",
    "5.5.5.5": "55555.com",
    "6.6.6.6": "66666.com",
    "7.7.7.7": "77777.com",
    "8.8.8.8": "88888.com",
    "9.9.9.9": "99999.com",
    "10.10.10.10": "101010.com"
}

# Запись в лог-файл
with open("ip.log", "w") as file:
    for _ in range(100):
        ip = random.choice(list(ip_dict.keys()))
        t = time.strftime("%H:%M:%S")
        kb = random.randint(100, 1000)
        dom_name = ip_dict[ip]

        log = f"{ip} - {t} - {kb} - {dom_name}\n"
        file.write(log)