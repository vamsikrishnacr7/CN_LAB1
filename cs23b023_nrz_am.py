import numpy as np
import matplotlib.pyplot as plt


# PART 1

seq = np.array([1, 0, 1, 0, 1, 1, 0])



def nrz(seq: np.array, bps: int):
    """
        function that converts a given sequence of bits to its NRZ encoding.
    """

    
    
    seq = seq * 2 - 1
    seq = np.repeat(seq, bps)
    return seq



NRZ = nrz(seq, 200)
print(len(NRZ))
print(f"The NRZ encoding for the sequence {seq} is: \n {NRZ}")

# PART 2

def create_carrier(freq, duration, sampling_rate, amplitude = 1, phase = 0):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint = False)
    wave = amplitude * np.sin(2 * np.pi * freq * t + phase)

    return t, wave


freq = 20.0  
s_rate = 1000.0 
dur = len(NRZ) /s_rate   


time, sine_wave = create_carrier(freq=freq, duration=dur, sampling_rate=s_rate)


plt.figure(figsize=(10, 4))
plt.plot(time, sine_wave)
plt.title(f'{freq} Hz Sine Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig("carrier_wave")


# PART 3

def amplitude_modulation(message, carrier):
    return message * carrier


amp_mod_wave = amplitude_modulation(NRZ, sine_wave)

plt.figure(figsize = (10, 12))

plt.subplot(3, 1, 1)
plt.title("Message wave")
plt.grid(True)
plt.plot(NRZ)

plt.subplot(3, 1, 2)
plt.title("Carrier wave")
plt.grid(True)
plt.plot(sine_wave)

plt.subplot(3, 1, 3)
plt.title("Amplitude Modulated wave")
plt.grid(True)
plt.plot(amp_mod_wave)

plt.savefig("amplots.pdf")






