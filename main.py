"""
# @Author : yuzhenliang
# @Date : 2020/11/18 0018 11:29
# @File : main.py
"""
# -*- coding:utf-8 -*-
import socket
import ssl

import node_info


def get_cert(hostname, ip, port, desired_SN):
    try:
        c = ssl.create_default_context()
        s = c.wrap_socket(socket.socket(), server_hostname=hostname)
        s.connect((ip, int(port)))
        send_data = 'GET / HTTP/1.1\r\nHost: ' + hostname + '\r\nConnection: close\r\n\r\n'
        s.send(bytes(send_data, encoding='utf-8'))
        cert = s.getpeercert()
        # s.getpeercert().items()
        if cert.get('serialNumber') == desired_SN:
            print(ip + "\'s HTTPS certificate is OK!")
        else:
            print(ip + "\'s HTTPS certificate is NOT OK! ")
            print(cert.items())
    except ssl.SSLCertVerificationError as e:
        print(ip + "\'s " + e.verify_message)
    except:
        print(ip + " OTHER ERROR!")


if __name__ == '__main__':
    hostname = 'act.migu.cn'
    #hostname = 'ugcyd.qq.com'
    port = '443'
    desired_SN = '08029ccffe1497e7df579116b5299255'.upper()
    #desired_SN = '0a954dd6683f3f9dce3b327d22f03f42'.upper()

    vips = input("请输入节点VIP（如多个节点，请以空格分隔）：").split(" ")
    while '' in vips:
        vips.remove('')

    for vip in vips:
        ips = node_info.ip_lists(vip)
        ips.sort()
        print("节点VIP：{0}\n节点设备数：{1}\n节点设备列表：{2}".format(vip, len(ips), "|".join(ips)))
        for ip in ips:
            get_cert(hostname, ip, port, desired_SN)
