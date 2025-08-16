def ccitt(data: bytes, initial_value: int = 0xFFFF, polynomial: int = 0x1021, xor_out: int = 0xFFFF) -> int:
    """
    Calculates the CRC-16-CCITT checksum for a given byte sequence.

    This implementation uses the polynomial 0x1021, an initial value of 0xFFFF,
    and a final XOR with 0xFFFF, which are common parameters for CRC-16-CCITT (X.25).

    Args:
        data: The input data as a bytes object.
        initial_value: The initial value for the CRC register. Common values are 0x0000 or 0xFFFF.
        polynomial: The CRC polynomial. For CRC-16-CCITT, it's typically 0x1021.
        xor_out: Value to XOR with the final CRC result. Often 0x0000 or 0xFFFF.

    Returns:
        The calculated 16-bit CRC checksum as an integer.
    """
    crc = initial_value  # Initialize the CRC register

    for byte in data:
        crc ^= (byte << 8)  # XOR the current byte (shifted left by 8 bits) into the CRC register

        for _ in range(8):  # Process each bit of the byte
            if (crc & 0x8000) != 0:  # Check if the MSB (most significant bit) is set
                crc = (crc << 1) ^ polynomial  # If MSB is set, shift left and XOR with polynomial
            else:
                crc = crc << 1  # If MSB is not set, just shift left
            crc &= 0xFFFF  # Ensure the CRC remains a 16-bit value (mask to 0xFFFF)

    return crc ^ xor_out # Final XOR operation