# Device DDoS
This DDoS tool serves to attack devices to receive packets. It allows someone to lose their internet quota, if this tool is used to attack their smartphone.

This tool does not apply to webstie attacks.

# Description
This directory contains Device DDoS scripts that you can use in a Linux environment.

## How to Use?
1. $ ``git clone https://github.com/anonimuslim/Device-DDoS``
2. $ ``cd Device-DDoS``
3. $ ``python2 Device-DDoS.py <ip> <port> <packet>``
4. $ ``python2 Device-DDoS.py 192.168.0.0 80 100`` (example)

The exemple is means that:
- IP target: 192.168.0.0
- port: 80
- Total of packet:100

### Suggestion for You
You can add except with a display like this for example "Stopping Attack!".

This is so that when the user closes the program (by pressing ctrl + c), the program can be closed neatly.

I'm still learning a lot about python programming, this program is also a recode from the [RCode777](https://github.com/RCode777) account. That way I still have a lot to learn python programming.

Alright, maybe that's enough. Thank you for your attention.
