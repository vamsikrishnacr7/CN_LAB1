import numpy as np

seq = np.array([1, 0, 1, 0, 1, 1, 0])



def nrz(seq: np.array, bps: int):
    """
        function that converts a given sequence of bits to its NRZ encoding.
    """

    
    
    seq = seq * 2 - 1
    seq = np.repeat(seq, bps)
    return seq



NRZ = nrz(seq, 2)
print(f"The NRZ encoding for the sequence {seq} is: \n {NRZ}")




