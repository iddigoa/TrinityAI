data = [
    {
        "deviceName": "Trinity_AI_Server#1",
        "type": "Server",
        "deviceType": "Linux",
        "model": "ProLiant DL380",
        "osType": "Ubuntu",
        "osVersion": "23.04",
        "vendor": "HPE",
        "ipAddress": "1.2.10.12",
        "macAddress": "001d.cv4c.fddd",
        "command": "route -n",
        "contents": """Kernel IP routing table
Destination Gateway Genmask Flags Metric Ref Use Iface
0.0.0.0 192.168.1.1 0.0.0.0 UG 0 0 0 eth0
192.168.1.0 0.0.0.0 255.255.255.0 U 0 0 0 eth0
10.0.0.0 0.0.0.0 255.0.0.0 U 0 0 0 eth1"""
    },
    {
        "deviceName": "Trinity_AI_Server#2",
        "type": "Server",
        "deviceType": "Linux",
        "model": "ProLiant DL380",
        "osType": "Ubuntu",
        "osVersion": "23.01",
        "vendor": "HPE",
        "ipAddress": "1.2.10.57",
        "macAddress": "001d.cv4c.f1dd",
        "contents" : """
Kernel IP routing table
Destination Gateway Genmask Flags Metric Ref Use Iface
0.0.0.0 192.168.1.1 0.0.0.0 UG 0 0 0 eth0
192.168.1.0 0.0.0.0 255.255.255.0 U 0 0 0 eth0
10.0.0.0 0.0.0.0 255.0.0.0 U 0 0 0 eth1        
        """   
    },
    {
        "deviceName": "Trinity_AI_Server#1",
        "type": "Server",
        "deviceType": "Linux",
        "model": "ProLiant DL380",
        "osType": "Ubuntu",
        "osVersion": "23.04",
        "vendor": "HPE",
        "ipAddress": "1.2.10.12",
        "macAddress": "001d.cv4c.fddd",
        "command": "ifconfig",
        "contents": """eth0      Link encap:Ethernet  HWaddr 00:0c:29:93:d5:4b
          inet addr:1.2.10.12  Bcast:1.2.10.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:10491 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10049 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:896218 (896.2 KB)  TX bytes:882261 (882.2 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:65536 errors:0 dropped:0 overruns:0 frame:0
          TX packets:65536 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:2621440 (2.6 MB)  TX bytes:2621440 (2.6 MB)"""
    },
    {
        "deviceName": "Trinity_AI_Server#2",
        "type": "Server",
        "deviceType": "Linux",
        "model": "ProLiant DL380",
        "osType": "Ubuntu",
        "osVersion": "23.01",
        "vendor": "HPE",
        "ipAddress": "1.2.10.57",
        "macAddress": "001d.cv4c.f1dd",
        "command": "",
        "contents": """eth0      Link encap:Ethernet  HWaddr 00:0c:29:93:d5:4b
          inet addr:1.2.10.57  Bcast:1.2.10.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:10491 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10049 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:896218 (896.2 KB)  TX bytes:882261 (882.2 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:65536 errors:0 dropped:0 overruns:0 frame:0
          TX packets:65536 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:2621440 (2.6 MB)  TX bytes:2621440 (2.6 MB)"""
    },
    {
        "deviceName": "Trinity_AI_Server#1",
        "type": "Server",
        "deviceType": "Linux",
        "model": "ProLiant DL380",
        "osType": "Ubuntu",
        "osVersion": "23.04",
        "vendor": "HPE",
        "ipAddress": "1.2.10.12",
        "macAddress": "001d.cv4c.fddd",
        "command": "rpm -q",
        "contents": """kernel-devel-5.17.1-200.fc37.x86_64
kernel-headers-5.17.1-200.fc37.x86_64
kernel-modules-5.17.1-200.fc37.x86_64
kernel-modules-extra-5.17.1-200.fc37.x86_64
glibc-common-2.35-15.fc37.x86_64
glibc-devel-2.35-15.fc37.x86_64
libstdc++-devel-10.3.1-3.fc37.x86_64
gcc-10.3.1-3.fc37.x86_64
gcc-c++-10.3.1-3.fc37.x86_64
make-4.3-5.fc37.x86_64
bash-5.1.18-1.fc37.x86_64
coreutils-8.32-27.fc37.x86_64
gawk-5.1.1-1.fc37.x86_64
patch-2.7.6-15.fc37.x86_64
zlib-1.2.11-29.fc37.x86_64
zlib-devel-1.2.11-29.fc37.x86_64"""
    },
    {
        "deviceName": "Trinity_AI_Server#2",
        "type": "Server",
        "deviceType": "Linux",
        "model": "ProLiant DL380",
        "osType": "Ubuntu",
        "osVersion": "23.01",
        "vendor": "HPE",
        "ipAddress": "1.2.10.57",
        "macAddress": "001d.cv4c.f1dd",
        "command": "rpm -q",
        "contents": """kernel-devel-5.17.1-200.fc37.x86_64
kernel-headers-5.17.1-200.fc37.x86_64
kernel-modules-5.17.1-200.fc37.x86_64
kernel-modules-extra-5.17.1-200.fc37.x86_64
glibc-common-2.35-15.fc37.x86_64
glibc-devel-2.35-15.fc37.x86_64
libstdc++-devel-10.3.1-3.fc37.x86_64
gcc-8.3.1-3.fc37.x86_64
gcc-c++-10.3.1-3.fc37.x86_64
make-4.3-5.fc37.x86_64
bash-5.1.18-1.fc37.x86_64
coreutils-8.32-27.fc37.x86_64
gawk-5.1.1-1.fc37.x86_64
patch-2.7.6-15.fc37.x86_64
zlib-1.2.11-29.fc37.x86_64
zlib-devel-1.2.11-29.fc37.x86_64"""
    },
    {
        "deviceName": "Trinity_AI_Server#1",
        "type": "Server",
        "deviceType": "Linux",
        "model": "ProLiant DL380",
        "osType": "Ubuntu",
        "osVersion": "23.04",
        "vendor": "HPE",
        "ipAddress": "1.2.10.12",
        "macAddress": "001d.cv4c.fddd",
        "command": "sysctl -a",
        "contents": """kernel.core_uses_pid = 1
kernel.domainname = localdomain
kernel.hostname = localhost
kernel.ostype = Linux
kernel.osrelease = 5.17.1-200.fc37.x86_64
kernel.osversion = #1 SMP Fri Aug 5 14:08:01 UTC 2023
kernel.version = 5.17.1-200.fc37.x86_64
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.rp_filter = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.conf.all.arp_announce = 2
net.ipv4.conf.all.arp_ignore = 1
net.ipv4.conf.all.arp_filter = 1
net.ipv4.conf.all.arp_accept = 2
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 1024
net.ipv4.tcp_synack_retries = 5
net.ipv4.tcp_syn_retries = 5
net.ipv4.tcp_max_orphans = 1024
net.ipv4.tcp_fin_timeout = 30"""
    },
    {
        "deviceName": "Trinity_AI_Server#2",
        "type": "Server",
        "deviceType": "Linux",
        "model": "ProLiant DL380",
        "osType": "Ubuntu",
        "osVersion": "23.01",
        "vendor": "HPE",
        "ipAddress": "1.2.10.57",
        "macAddress": "001d.cv4c.f1dd",
        "command": "sysctl -a",
        "contents": """kernel.core_uses_pid = 1
kernel.domainname = localdomain
kernel.hostname = localhost
kernel.ostype = Linux
kernel.osrelease = 5.17.1-200.fc37.x86_64
kernel.osversion = #1 SMP Fri Aug 5 14:08:01 UTC 2023
kernel.version = 5.17.1-200.fc37.x86_64
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.rp_filter = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.conf.all.arp_announce = 2
net.ipv4.conf.all.arp_ignore = 1
net.ipv4.conf.all.arp_filter = 1
net.ipv4.conf.all.arp_accept = 2
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 512
net.ipv4.tcp_synack_retries = 5
net.ipv4.tcp_syn_retries = 5
net.ipv4.tcp_max_orphans = 1024
net.ipv4.tcp_fin_timeout = 30"""
    }
]

