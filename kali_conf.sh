# Set some variables that needs to be set in Kali Linux
export LANGUAGE=en_US.UTF-8                
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Update and upgrade the packets
sudo apt-get update && sudo apt-get upgrade 

# Install RDP
sudo apt install xrdp
sudo update-rc.d xrdp enable
sudo service xrdp start

# Check status of xrdp
# sudo service xrdp status

# Add a rdp user
sudo adduser --home /rdp rdp
sudo usermod -aG sudo rdp

# enable xrdp
sudo systemctl enable xrdp
sudo service xrdp status
