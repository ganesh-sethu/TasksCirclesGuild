# LINUX SHELL COMMANDS CHEAT SHEET

## Basic Navigation:
- `pwd` - show current directory
- `ls` - list files
- `ls -l` - detailed list
- `ls -la` - include hidden files
- `cd directory` - change directory
- `cd ~` - go home
- `cd ..` - go up one level
- `cd -` - go to previous directory

## File Operations:
- `touch filename` - create empty file
- `mkdir dirname` - create directory
- `mkdir -p path/to/dir` - create nested directories
- `cp source dest` - copy file
- `cp -r source dest` - copy directory
- `mv source dest` - move or rename
- `rm filename` - delete file
- `rm -r dirname` - delete directory
- `rmdir dirname` - remove empty directory

## View Files:
- `cat filename` - show entire file
- `less filename` - view page by page
- `head filename` - show first 10 lines
- `head -20 filename` - show first 20 lines
- `tail filename` - show last 10 lines
- `tail -f filename` - follow file changes

## Redirection:
- `command > file` - save output to file
- `command >> file` - append output to file
- `command1 | command2` - pipe output
- `command 2>&1` - redirect errors too

## Wildcards:
- `*` - match any characters
- `?` - match single character
- `[abc]` - match a, b, or c
- `[a-z]` - match lowercase letters

## Help:
- `man command` - manual for the command
- `command --help` - help to use the command
- `whatis command` - description of the command
- `which command` - location of the command

## Search and Process Text:
- `grep pattern file` - search for text
- `grep -i pattern file` - case insensitive search
- `grep -r pattern dir` - search in directory
- `wc filename` - count words/lines
- `sort filename` - sort lines
- `uniq filename` - remove duplicates

## Change Permissions:
- `chmod 755 filename` - set permissions (rwxr-xr-x)
- `chmod +x filename` - add execute permission
- `chmod -w filename` - remove write permission
- `chmod u+rwx filename` - user read/write/execute
- `chmod g+rw filename` - group read/write
- `chmod o-r filename` - remove others read

## Permission Numbers:
- r (read) = 4
- w (write) = 2
- x (execute) = 1

**Common combinations:**
- 755 = rwxr-xr-x (owner full, others read/execute)
- 644 = rw-r--r-- (owner read/write, others read only)
- 777 = rwxrwxrwx (full permissions for all)

## User Info:
- `whoami` - current username
- `id` - user and group IDs
- `who` - who is logged in
- `w` - detailed user activity

## Process Management:
- `ps` - show processes
- `ps aux` - detailed process list
- `top` - real-time process monitor
- `htop` - better process monitor
- `jobs` - show background jobs
- `bg` - put job in background
- `fg` - bring job to foreground
- `kill PID` - kill process by ID
- `kill -9 PID` - force kill process
- `killall processname` - kill all processes by name
- `nohup command &` - run command in background

## Package Management

### Debian/Ubuntu (apt):
- `sudo apt update` - update package list
- `sudo apt upgrade` - upgrade packages
- `sudo apt install pkg` - install package
- `sudo apt remove pkg` - remove package
- `sudo apt search pkg` - search for package

### Red Hat/CentOS (yum):
- `sudo yum update` - update packages
- `sudo yum install pkg` - install package
- `sudo yum remove pkg` - remove package
- `sudo yum search pkg` - search packages

## Network Tools:
- `ping hostname` - test connectivity
- `ping -c 4 hostname` - ping 4 times
- `wget url` - download file
- `curl url` - get data from server
- `ifconfig` - network interface info
- `ip addr show` - show IP addresses
- `netstat -tuln` - show listening ports

## File Transfer:
- `scp file user@host:path` - copy to remote server
- `scp user@host:file .` - copy from remote server
- `rsync -av source dest` - sync directories

## System Details:
- `uname -a` - system information
- `uname -r` - kernel version
- `uptime` - system uptime
- `date` - current date/time
- `cal` - calendar
- `history` - command history

## Disk and Memory:
- `df -h` - disk space usage
- `du -h directory` - directory size
- `free -h` - memory usage
- `lsblk` - list storage devices

## Hardware:
- `lscpu` - CPU information
- `lsusb` - USB devices
- `lspci` - PCI devices

## Find Files:
- `find /path -name "*.txt"` - find files by name
- `find /path -type f` - find files only
- `find /path -size +100M` - find large files
- `locate filename` - fast file search
- `which command` - find command location

## Service Management:
- `sudo systemctl start service` - start service
- `sudo systemctl stop service` - stop service
- `sudo systemctl status service` - check service status
- `sudo systemctl enable service` - enable at boot

## View Logs:
- `sudo tail -f /var/log/syslog` - follow system log
- `sudo journalctl -f` - follow journal