from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
import threading
from scapy.layers.l2 import Ether
import os


def read_filter_rules(filter_file):
    """
    读取过滤规则
    """
    rules = []
    with open(filter_file, "r") as f:
        for line in f.readlines():
            rule = line.strip().split(" ")
            if len(rule) == 3 and (rule[0] == "permit" or rule[0] == "deny") and rule[1] == "source":
                action = rule[0]
                src_address = rule[2]
                dst_address = "any"
                rules.append((action, src_address, dst_address))
    return rules


def write_filter_rules(filter_file, rules):  # 写入过滤规则

    with open(filter_file, "w") as f:
        for rule in rules:
            f.write(f"{rule[0]} source {rule[1]}\n")


def add_rule(rules):  # 添加规则
    action = input("输入 permit 或 deny：")
    src_address = input("输入源地址：")
    dst_address = "any"
    rules.append((action, src_address, dst_address))
    write_filter_rules(
        "C:\\Users\\逐星i\\OneDrive\\桌面\\PythonCode\\PycharmProjects\\pythonProject\\My_project\\Learn\\Firewall\\Rule.txt",
        rules)
    print(f"已添加规则：{action} source {src_address} -> {dst_address}")


def del_rule(rules):  # 删除规则
    idx = int(input("输入要删除规则的索引："))
    new_rules = []
    for i, rule in enumerate(rules):
        if i != idx:
            new_rules.append(rule)
        else:
            print(f"已删除规则：{rule[0]} source {rule[1]} -> {rule[2]}")
    write_filter_rules(
        'C:\\Users\\逐星i\\OneDrive\\桌面\\PythonCode\\PycharmProjects\\pythonProject\\My_project\\Learn\\Firewall\\Rule.txt',
        new_rules)


def forward_packet(pkt):  # 转发数据包

    # 修改数据包中的MAC地址和IP地址（将源地址改为目标地址，目标地址改为源地址）
    pkt[Ether].src, pkt[Ether].dst = pkt[Ether].dst, pkt[Ether].src
    pkt[IP].src, pkt[IP].dst = pkt[IP].dst, pkt[IP].src
    # 发送数据包到网络接口
    sendp(pkt, iface=pkt.sniffed_on)


def drop_packet(pkt):  # 直接丢弃数据包

    # 丢弃数据包
    pass


def process_packet(p, rules):  # 处理数据包

    # 根据源 IP 地址匹配过滤规则
    matched = any(
        (rule[0] == "permit") and
        ((rule[1] == "any") or (p[IP].src == rule[1]))
        for rule in rules
    )

    if matched:
        forward_packet(p)
    else:
        drop_packet(p)


def start_firewall(rules):  # 启动防火墙程序

    # 获取要监听的设备对应网口的名称
    iface = 'Intel(R) Wi-Fi 6 AX200 160MHz'

    # 使用sniff函数捕获数据包，并将其传递给回调函数进行处理
    sniff(prn=lambda x: process_packet(x, rules), store=0, iface=iface)


def main():
    """
    主程序入口
    """

    # 读取过滤规则
    rules = read_filter_rules(
        'C:\\Users\\逐星i\\OneDrive\\桌面\\PythonCode\\PycharmProjects\\pythonProject\\My_project\\Learn\\Firewall\\Rule.txt'
    )

    # 启动防火墙程序
    firewall_thread = threading.Thread(target=start_firewall, args=(rules,))
    firewall_thread.start()

    while True:
        os.system("cls" if os.name == "nt" else "clear")  # 清除终端输出
        user_choice = input("\n输入数字以进行其他操作：\n1. 查看所有规则\n2. 增加规则\n3. 删除规则\n4. 停止防火墙\n")
        if user_choice == "1":
            print("当前规则：")
            for rule in rules:
                print(f"{rule[0]} source {rule[1]} -> {rule[2]}")
            continue
        elif user_choice == "2":
            try:
                add_rule(rules)
            except Exception as e:
                print(f"添加规则时发生错误：{e}")
            continue
        elif user_choice == "3":
            try:
                del_rule(rules)
            except Exception as e:
                print(f"删除规则时发生错误：{e}")
            continue
        elif user_choice == "4":
            break
        else:
            print("输入错误！！！请按规则输入")
            continue

    # 等待防火墙线程结束
    firewall_thread.join()

    # 退出整个程序
    sys.exit(0)


if __name__ == "__main__":
    main()
