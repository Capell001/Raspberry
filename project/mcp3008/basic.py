from gpiozero import MCP3008
from time import sleep

if __name__ == "__main__":
    channel0 = MCP3008(0)
    while(True):
        value = channel0.value
        print("now value:{}".format(value))
        sleep(1)