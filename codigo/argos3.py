import argos3
import numpy as np 

# Frequência da portadora (entre 1kHz e 8kHz)
fc = np.random.randint(10,80)*100

# Exibe a frequência da portadora
print(fc)
2400

# Cria o transmissor e transmite o datagrama gerando o sinal s(t)
transmitter = argos3.Transmitter(fc=fc)
t, s = transmitter.transmit(argos3.Datagram(pcdnum=1234, numblocks=1))

# Cria o canal com duração de 1 segundo
channel = argos3.Channel(duration=1, noise_mode="ebn0", noise_db=20)
# Adiciona o sinal no meio do canal
channel.add_signal(s, position_factor=0.5)
channel.add_noise()
st = channel.channel

# Cria o detector de portadora e detecta as transmissões contidas no canal
detector = argos3.CarrierDetector(seg_ms=10, threshold=-15)
detector.detect(st.copy())
detections = detector.return_channels()

# Exibe as detecções no formato (fc, start_seg, end_seg)
print(detections)
[(np.float64(2400.0), 41, 65)]

# Isola o sinal recebido s'(t) a partir das amostras de início e fim da detecção
first_sample = int((detections[0][1] - detector.history) * detector.fs * detector.seg_s)
last_sample = int(detections[0][2] * detector.fs * detector.seg_s)
st_prime = st[first_sample:last_sample]

# Cria o receptor, recebe o sinal s'(t) e tenta decodificar o datagrama
receiver = argos3.Receiver(fc=detections[0][0])
datagramRX, success = receiver.receive(st_prime)

# Exibe se a recepção foi bem sucedida e o datagrama recebido
print(success)
True
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