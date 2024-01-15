#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-7
#
import netifaces as ni

def get_local_ip():
    local_ips = []
    for interface in ni.interfaces():
        # 排除回环接口
        if 'lo' in interface or 'bridge' in interface:
            continue
        try:
            # 获取接口的 IPv4 地址
            ipv4 = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
            local_ips.append(ipv4)
            break
        except (ValueError, KeyError, IndexError):
            pass
    return local_ips

if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        print(f"Local IP Address: {local_ip}")
    else:
        print("Failed to retrieve local IP.")
