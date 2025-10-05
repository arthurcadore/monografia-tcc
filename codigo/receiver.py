import argos3
import numpy as np 

datagramTX = argos3.Datagram(pcdnum=1234, numblocks=1)
t, s = argos3.Transmitter().transmit(datagramTX)

datagramRX, success = argos3.Receiver().receive(s)
print(datagramRX.parse_datagram())
{
  "msglength": 1,
  "pcdid": 1234,
  "data": {
    "bloco_1": {
      "sensor_1": 37,
      "sensor_2": 198,
      "sensor_3": 9
    }
  },
  "tail": 7
}