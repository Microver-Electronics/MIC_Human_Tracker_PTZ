sudo chmod 666 /dev/ttyS0
sudo chmod 666 /dev/ttyS1

sudo insmod /usr/lib/modules/5.15.0-56-generic/kernel/drivers/gpio/gpio-f7188x.ko

sudo echo out > /sys/class/gpio/gpio80

sudo echo out > /sys/class/gpio/gpio81

sudo echo out > /sys/class/gpio/gpio82
