import argos3
import numpy as np 

fc = np.random.randint(10,80)*100 # print(fc) -> 2400
transmitter = argos3.Transmitter(fc=fc)
t, s = transmitter.transmit(argos3.Datagram(pcdnum=1234, numblocks=1))

channel = argos3.Channel(duration=1, noise_mode="ebn0", noise_db=20)
channel.add_signal(s, position_factor=0.5)
channel.add_noise()

detector = argos3.CarrierDetector(seg_ms=10, threshold=-15)
detector.detect(channel.channel.copy())
detections = detector.return_channels() # print(detections) ->  [(np.float64(2400.0), 41, 65)]
                  
first_sample = int((detections[0][1] - 5) * detector.fs * detector.seg_s)
last_sample = int(detections[0][2] * detector.fs * detector.seg_s)
st_prime = channel.channel[first_sample:last_sample]

receiver = argos3.Receiver(fc=detections[0][0])
datagramRX, success = receiver.receive(st_prime) # print(success) -> True