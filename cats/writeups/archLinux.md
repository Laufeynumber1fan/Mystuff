I was interested in making an Arch Linux VM because of this [tierlist](https://www.dvlv.co.uk/my-linux-distro-tier-list.html) I found as part of my virtual network for pcap analysis. After downloading the Arch iso I went into a rabbit hole after booting up the Arch VM and seeing a root terminal prompting me for commands.

![alt text](https://github.com/Laufeynumber1fan/Mystuff/blob/main/src/images/cats/screenshot-archlinux.png)

Apparently upon an initial boot of a new Arch machine, you actually have to initialize and install Arch from scratch via command line. This is usually done for most other distributions automatically with some sort of installation menu upon first boot. But not Arch!

After writing this guide and installing arch properly I still can't believe I have taken for granted those installation menus.

So I followed through the [installation guide for Arch](https://wiki.archlinux.org/title/Installation_guide) but I decided to make my own guide for my notes whenever the knowledge escapes me. Here are my steps:
  
1. First of all, I made the new VM, I left all the default options on except I gave it lots of disk space (16GB) and lots of RAM then I went into Virtual Machine Settings > Options > Advanced > Firmware type > set to UEFI. This sets it to UEFI booting.
  
2. An initial step is to configure network settings, do `ip a` to check if VMware already gave Arch an IP.

If it doesn't have one go to the [systemd-networkd page](https://wiki.archlinux.org/title/Systemd-networkd#Configuration_files) in the same Arch Wiki to properly configure the networkd service with a conf file on terminal. I use `nano /etc/systemd/network/20-ethernet.network` to edit one of the config profiles but editing/making a new conf file in that directory will do.
  
Inside the .network file you need these lines:
```
[Match]
Name=[interface name]
#or
Name=en*
```
```
[Network]
DHCP=yes
```
  
This enables the interface to accept DHCP leases. VMware provides DHCP in the subnet I made. Do `systemctl restart systemd-networkd.service` to then restart networkd so it can apply the new config settings.
  
3. Do `ping 8.8.8.8` to verify the VM has network connection.
  
4. The next major step is to partition the virtual disk. By doing `fdisk -l` to display the current disks I see /dev/sda and /dev/loop0. I can safely assume that /dev/loop0 contains the Arch iso and that /dev/sda is the virtual disk given to me by VMware and is the disk that I will have to partition.
  
5. I highly recommend making a VM snapshot if you haven't already, afterwards I use `parted /dev/sda` to step into that disk and begin partitioning.
  
6. It is crucial to have understanding on blocks and sectors present on disk drives. Articles that helped me are [here](https://wiki.archlinux.org/title/Partitioning#Partition_alignment) and [here](https://askubuntu.com/questions/701729/partition-alignment-parted-shows-warning).
  
By doing `fdisk -l` again. I can see that VMware gave me 8GiB that I need to partition and mount.
  
I need to achieve 3 goals:
- For starters, I need a partition table. I decide on using gpt, since I'm using gpt I need an efi partition, since I need an efi partition it needs to be a FAT32 partition type and it also needs to be 1GiB based on this [example](https://wiki.archlinux.org/title/Installation_guide#Example_layouts).  
- Next I want a [swap partition](https://opensource.com/article/18/9/swap-space-linux-systems) to boost performance (this VM might be opening some big pcaps) so good size for a swap partition is twice the amount of RAM which will be 2GiB.
- And finally I want ext4 for my / directory which I will store my user files. The ext4 partition will start from 3GiB to 14GiB in the disk drive. The remaining 2 GiB will be free space to reduce fragmentation.
  
To actually partition my disk on the VM machine I will be using `parted`. I do `parted /dev/sda` to enter the shell for that disk.
`mklabel gpt` to set the partition table.
`unit MiB` to set the u
`mkpart primary fat32 1024KiB 1024MiB` to make a FAT32 partition for the EFI /boot dir.
`mkpart primary linux-swap 1GiB 3GiB` to make a 2GiB linux swap partition.
`mkpart primary ext4 3GiB 14GiB` to make an 11 GiB / ext4 file dir.
  
Then I use `print free` to verify the used and remaining disk space. And then do `quit`.
  
7. The next step is to have Arch recognise my swap partition.  
`mkswap /dev/sda2` to initialise that drive. Use `fdisk -l` again to verify which one is the swap partition.  
`swapon /dev/sda2` to add the swap drive into /etc/fstab  
`swapon --show` to verify if the swap drive shows up.  
  
8. /dev/sda1 and /dev/sda3 are partitioned but empty. To initialise the file systems, use `mkfs`.  
`mkfs.ext4 /dev/sda3`  
`mkfs.fat -F 32 /dev/sda1`  
  
9. Now to mount these 2 drives to VM according to the [install guide](https://wiki.archlinux.org/title/Installation_guide#Mount_the_file_systems).  
`mount /dev/sda3 /mnt`  
`mount --mkdir /dev/sda1 /mnt/boot`  
  
10. Next step is to download the linux firmware that will occupy the partitioned drive. These packages in addition to the Arch ISO make up the Arch linux OS. I did a quick `cat /etc/pacman.d/mirrorlist` to check the mirrors. Then I used `pacstrap`.  
`pacstrap -K /mnt base linux linux-firmware`  
  
11. This is done to copy the fstab file of the root terminal to the fstab of the / directory. fstab is for saving drive partition configuration.
`genfstab -U /mnt >> /mnt/etc/fstab`  
  
12. `arch-chroot /mnt` to su into the root user of the / directory.
  
13. Next I use `pacman` to download additional packages for the Arch OS. I tried adding as much as I can but I know I'm gonna have to install more. To install with pacman it's `pacman -S [package name]`.  
`pacman -S sudo man-db man-pages texinfo nano amd-ucode nmap systemd grub efibootmgr`  
Make sure you are in the / directory by doing the previous step. The last two packages are critical because they will be the UEFI bootloader which I configured on step 1.
  
14. Additional configurations are needed for time and keyboard.
  
`ln -sf /usr/share/zoneinfo/Canada/Eastern /etc/localtime` to set it to Eastern timezone.  
`hwclock --systohc` to set Arch to use UTC time.  
`timedatectl set-timezone Canada/Eastern` to set it to Eastern timezone again.  
Verify the time is correct with `timedatectl status`.  
  
Since I installed nano, I use `nano /etc/locale.gen` to edit the locale config.
Inside the locale.gen do `Ctrl + F` and search for `#en_US.UTF-8 UTF-8` and take out the `#` on that line to uncomment it.  
To exit out of nano do `Ctrl + X` and hit `Y` to save.  
`locale-gen` to regenerate with the new locale file.  
  
Next is to set an environment variable to set the locale again. Do `nano /etc/locale.conf` to make a new file and add:
```
# Custom
LANG=en.US.UTF-8
```
Then save and exit.

15. To set a root password.
`passwd`  
  
16. Now one of the most crucial steps is to install a bootloader.
Checklist before you configure [GRUB](https://wiki.archlinux.org/title/GRUB#), the bootloader I chose.
- Make sure `grub` and `efibootmgr` is installed
- Optionally, do a snapshot 
- `ls boot` to check if /dev/sda1 is not empty. If it is then get out of chroot then do `mount /dev/sda1 /mnt/boot` to remount the boot drive again. `arch-chroot /mnt` to get back

I installed grub in /mnt/boot. Do this command while in / dir.
`grub-install --target=x86_64-efi --efi-directory=boot --bootloader-id=GRUB`
If you encounter errors, revert to snapshot and then debug. If it says no errors then proceed.

`ls boot` to verify grub was installed.
`grub-mkconfig -o /boot/grub/grub.cfg` to save the grub configurations.

17. It should all be done. Restart the VM or `exit` + `reboot` and arch linux should show up as the boot option in the UEFI menu. Confirm on the boot menu to start arch linux and you'll have Arch Linux installed.
  
BUT WAIT! There are additional configurations.
The fresh install of Arch has no GUI and no network configuration.
  
18. Refer to step 2 network configuration because the networkd settings are empty for the /root dir.
After making a .network config file, the service networkd needs to start on boot.
`systemctl enable systemd-networkd.service` to enable it, `enable` saves it a startup process.
`systemctl start systemd-networkd.service` to start it just once.
  
In addition, I also needed to configure the DNS settings.
`nano /etc/resolv.conf` and type `nameserver 8.8.8.8` to set google.com as a DNS server.
Instead of pinging 8.8.8.8, do `ping google.com` to confirm that DNS is working.
  
19. For the desktop environment I choose [KDE](https://wiki.archlinux.org/title/KDE).  
`pacman -S plasma-desktop plasma-firewall sddm konsole firefox` to install, confirm default options.

20. A user is necessary to access arch beyond just the root account.
`useradd -m arch` to make a user named arch. `-m` gives it a home directory.
`passwd arch` to give it a password

To give it sudo privileges, do `EDITOR=nano visudo` to edit the sudoers file.
`Ctrl + -` and type 122 to jump to the user privileges line and type on a blank line `arch ALL=ALL` to give the new arch user sudo privileges on all commands.
Go to line 47 and add `Defaults !lecture` to a new line to disable sudo lectures.
`systemctl enable systemd-homed` + `systemctl start systemd-homed` to start a utility for recognising home dirs and sudoers users on that file.
  
21. Finally, to initialise the desktop environment I installed on step 19 I do the last few commands.
`systemctl enable sddm.service`
`systemctl start sddm.service`

Search konsole for the terminal!