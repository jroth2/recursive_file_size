import os


def get_file_size_formatted(path: str, unit:str, precision: int = 2):
    return convert_from_bytes(os.path.getsize(path),unit,precision)

def get_file_size(path: str) -> int:
    return os.path.getsize(path)

def convert_from_bytes(bytes: int, unit:str, precision: int = 2) -> float:
    """
    Docstring for convert_from_bytes
    
    :param bytes: Number of bytes to be converted
    :type bytes: int
    :param unit: Unit to convert to e.g. KB, MB, GB, or TB
    :type unit: str
    :return: Returns a float containing the new unit type to n positions
    :rtype: float
    :param precision Number of precision for rounding, default 2 pos
    :type precision: int
    """

    kilobytes = ['KILOBYTE','KILOBYTES','KB']
    megabytes = ['MEGABYTE','MEGABYTES','MB']
    gigabytes = ['GIGABYTE','GIGABYTES','GB']
    terabytes = ['TERABYTE','TERABYTES','TB']
    if unit.upper() in kilobytes:
        exponent = 1
    elif unit.upper() in megabytes:
        exponent = 2
    elif unit.upper() in gigabytes:
        exponent = 3
    elif unit.upper() in terabytes:
        exponent = 4

    return round(bytes/1000**exponent,precision)





if __name__=='__main__':
    #print(get_file_size("file_size.py"))
    #print(get_file_size("/Users/joe/Documents/sav2.sav"))
    #print(get_file_size('/Users/joe/Downloads/ Shelby Van Pelt - Remarkably Bright Creatures.epub'))
    #print(get_file_size('/Users/joe/Downloads/2021-05-07-raspios-buster-armhf-lite.img'))
    path = '/Users/joe/Downloads/2021-05-07-raspios-buster-armhf-lite.img'
    print(get_file_size_formatted(path,'GB',1))



