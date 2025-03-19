I was interested in making an Arch Linux VM because of this [tierlist](https://www.dvlv.co.uk/my-linux-distro-tier-list.html) I found as part of my virtual network for pcap analysis. After downloading the Arch iso I went into a rabbit hole after booting up the Arch VM and seeing a root terminal prompting me for commands.

![alt text](https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/screenshot-archlinux.png)

Apparently upon an initial boot of a new Arch machine, you actually have to initialize and install Arch from scratch via command line, this is usually done for most other distributions automatically with some sort of installation menu upon first boot and this is something that I have taken for granted most of my life with my newfound inexperience in trying to install an OS like Arch.

Below are some of the things I learned when I was learning how to install Arch:

I followed through the [installation guide for Arch](https://wiki.archlinux.org/title/Installation_guide) and it was simple enough to follow but I quickly ran through a roadblock at systemd-networkd on section 1.7.
This was Arch telling me to do network configuration through the root terminal, here were the steps I took:

1. I used VMWare as I am familiar with its virtual switching. I added the Arch VM to a NAT subnet on 192.168.242.0/24.
2. I referred to the [systemd-networkd page](https://wiki.archlinux.org/title/Systemd-networkd#Configuration_files) in the same Arch Wiki to properly configure the networkd service with a conf file on terminal. I used `nano /etc/systemd/network/20-ethernet.network` to edit one of the config profiles but editing/making a new conf file in that directory will do.

Inside the .network file you need these lines:
```
[Match]
Name=[interface name]
#or
Name=en*
```
To select the interface. If you don't know the interface name use `ip a`. If you don't see an ethernet adapter check if the VM was given one on the VM network settings.
```
[Network]
DHCP=yes
```
This enables the interface to accept DHCP leases. VMware provides a DHCP server in the subnet I made. 
3. Do `systemctl restart systemd-networkd.service` to then restart networkd so it can apply the new config settings. Do `ip a` and `ping 8.8.8.8` to verify the VM has network connection.
4. The next major step is to partition the virtual disk. By doing `fdisk -l` to display the current disks I see /dev/sda and /dev/loop0. I can safely assume that /dev/loop0 contains the Arch iso and that /dev/sda is the virtual disk given to me by VMware and is the disk that I will have to partition.
5. I highly recommend making a VM snapshot if you haven't already, afterwards I use `parted /dev/sda` to step into that disk and begin partitioning.
6. 