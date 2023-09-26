import subprocess

import sys

import os

if __name__ == '__main__':
    pcap_root_path = '/Users/yzsong/data/graduation-project/pcaps/ssr-pcaps'
    stat = {}
    for root, ds, fs in os.walk(pcap_root_path):
        for d in ds:
            dir_path = os.path.join(root, d)
            for dir_root, _, fss in os.walk(dir_path):
                for f in fss:
                    if f.endswith(".pcap"):
                        pcap_file = os.path.join(dir_path, f)
                        pcap_file = os.path.abspath(pcap_file)
                        print("hello")
                        output = subprocess.check_output(f"tcpdump -n -r {pcap_file} | wc -l", shell=True)
                        # print(os.system(f"tcpdump -n -r {pcap_file} | wc -l"))
                        if stat.get(dir_root) is None:
                            stat[dir_root] = 0
                        print(int(output.decode()))
                        stat[dir_root] += int(output.decode())

    print(stat)          # sys.exit()

