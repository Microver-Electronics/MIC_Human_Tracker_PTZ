class Auxiliary():

    def __init__(self, *args, **kwargs):
        pass

    def hexfmt(self, val):
        """
        Description : this function converts decimal value to 1byte hex value
        """
       
        return '0x{:04X}'.format(val)

    def scale(self, val, src, dst):
        """
        Scale the given value from the scale of src to the scale of dst.
        """

        return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

    def sum_of_hex_list_mod256(self, hex_list):

        hex_to_decimal_list = []

        [hex_to_decimal_list.append(int(x, 16)) for x in hex_list]
        
        result = self.hexfmt((sum(hex_to_decimal_list)%256))[2:]

        return result