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
  

6. It is crucial to have understanding on blocks and sectors present on disk drives. Articles that helped me are [here](https://wiki.archlinux.org/title/Partitioning#Partition_alignment) and [here](https://askubuntu.com/questions/701729/partition-alignment-parted-shows-warning).
  
By doing `fdisk -l` again. I can see that VMware gave me 8GiB that I need to partition and mount.
  
I need to achieve 3 goals:
- For starters, I need a partition table. I decide on using gpt, since I'm using gpt I need an efi partition, since I need an efi partition it needs to be a FAT32 partition type and it also needs to be 1GiB based on this [example](https://wiki.archlinux.org/title/Installation_guide#Example_layouts).  
- Next I want a [swap partition](https://opensource.com/article/18/9/swap-space-linux-systems) to boost performance (this VM might be opening some big pcaps) so good size for a swap partition is twice the amount of RAM which will be 2GiB.
- And finally I want ext4 for my / directory which I will store my user files. The ext4 partition will start from 3GiB to 7GiB in the disk drive. The remaining 1 GiB will be free space to reduce fragmentation.
  
To actually partition my disk on the VM machine I will be using `parted`. I do `parted /dev/sda` to enter the shell for that disk.
`mklabel gpt` to set the partition table.
`mkpart primary fat32 1024KiB 1024MiB` to make a FAT32 partition for the EFI /boot dir.
`mkpart primary linux-swap 1GiB 3GiB` to make a 2GiB linux swap partition.
`mkpart primary ext4 3GiB 7GiB` to make a 4GiB / ext4 file dir. 

Then I use `print free` to verify the used and remaining disk space. And then do `quit`.
  

7. The next step is to have Arch recognise my swap partition.  
`mkswap /dev/sda2` to initialise that drive. Use `fdisk -l` again to verify which one is the swap partition.  
`swapon /dev/sda2` to add the swap drive into /etc/fstab  
`swapon --show` to verify if the swap drive shows up.  
  

8. /dev/sda1 and /dev/sda3 are partitioned but empty. To initialise the file systems, use `mkfs`.  
`mkfs.ext4 /dev/sda3`  
`mkfs.fat -F 32 /dev/sda1`  
  

9. Now to mount these 2 drives to VM according to the [guide](https://wiki.archlinux.org/title/Installation_guide#Mount_the_file_systems).  
`mount /dev/sda3 /mnt`  
`mount --mkdir /dev/sda1 /mnt/boot`  
  

10. Next step is to download the linux firmware that will occupy the partitioend drive. These packages in addition to the Arch ISO make up the Arch linux OS. I did a quick `cat /etc/pacman.d/mirrorlist` to check the mirrors. Then I used `pacstrap`.  
`pacstrap -K /mnt base linux linux-firmware`  
