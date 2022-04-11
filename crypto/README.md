# Guide to setup Crypto Miner
## Raspberry Pi Zero W

This project assumes the installation of Raspberry pi lite and successful setup of wpa_supplicant and ssh.

## Setup

After connecting via ssh enter into the console to run the usual updates

`sudo apt-get update && sudo get-get upgrade -y`

Once the updates are complete, install the below dependencies:

`sudo apt install git automake autoconf libcurl4-openssl-dev libjansson-dev libssl-dev libgmp-dev`

I used Monero and cpuminer-multi for this project. You will need to download the below repository from them.

`sudo git clone https://github.com/carolinedunn/cpuminer-multi`

Once downloaded navigate to the directory

`cd cpuminer-multi`

Next we need to compile the code using the following commands:

`sudo ./autogen.sh`

`sudo ./configure`

`sudo ./build.sh`

This will take quite a while, particurarly build.sh, just let it run.

## Mining Monero 

Once this is all done, run the follwing command to begin mining. 

`./cpuminer -a cryptonight -o stratum+tcp://pool.minexmr.com:443 -u YOUR_EMAIL_ADDRESS`

Should see some numbers here about the hashes per minute. On the Pi Zero I get about 1.47. Interesting in the future is to consider a cluster of pi zeroes to see if I can mine enough to offset the cost.

If there is a connection refused or timeout. Try on other ports allowed on that pool. It is also possible the pool above is no longer in use
