# NRZ Encoding and Amplitude Modulation

This code implements a digital communication simulation involving **Non-Return-to-Zero (NRZ)** encoding and **Amplitude Modulation (AM)** using Python.

## Details
- **Sequence**: `[1, 0, 1, 0, 1, 1, 0]`
- **Bits per Sample**: 200
- **Carrier Frequency ($f_c$)**: 20 Hz
- **Sampling Rate ($f_s$)**: 1000 Hz
- **Encoding Scheme**: NRZ (+1 for bit 1, -1 for bit 0)

## Technical Implementation

1. **Part 1: NRZ Encoding**
   - Converts the binary input array into a signal where 1s are +1 and 0s are -1.
   - Uses `np.repeat` to extend the signal based on the bits-per-sample (bps) requirement.
2. **Part 2: Carrier Signal Generation**
   - Generates a sinusoidal carrier wave using a time array synchronized with the message length.
   - Ensures the duration ($dur$) is calculated as `len(NRZ) / sampling_rate` to avoid array broadcasting errors.
3. **Part 3: Amplitude Modulation**
   - Performs modulation by multiplying the NRZ message signal with the carrier signal.
   - This results in a Phase/Amplitude Shift Keying representation of the digital data.

## Visualizations
The script generates a multi-panel plot saved as `amplots.pdf` containing:
- **Message Signal**: The square-wave NRZ encoded bits.
- **Carrier Signal**: The 20 Hz high-frequency sine wave.
- **AM Modulated Signal**: The resulting modulated wave showing phase/amplitude transitions.

## Instructions to Run
1. Ensure [NumPy](numpy.org) and [Matplotlib](matplotlib.org) are installed.
2. Run the script using the following command:
   ```bash
   python3 cs23b023_nrz_am.py
