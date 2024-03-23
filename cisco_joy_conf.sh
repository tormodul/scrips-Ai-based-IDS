# Install dependencies
sudo apt-get install build-essential libssl-dev libpcap-dev libcurl4-openssl-dev

# check the verison of openssl
# openssl version

# Download Joy
git clone https://github.com/cisco/joy.git
cd joy

# Configure the package
./configure --enable-gzip

# Builded the package
make clean;make

# Use the package
sudo bin/joy interface=eth0 bidir=1 entropy=1 output=test2.json

# If it is in a weird format, its probably zipped.
mv test2.json test2.json.gz
gunzip Ddos1.json.gz
cat Ddos1.json
