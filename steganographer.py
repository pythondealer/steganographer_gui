"""

original code written by : Priyansh Anand
E-Mail          : contact.priyanshanand@gmail.com & developer.priyanshanand@gmail.com
GitHub          : https://github.com/priyansh-anand

modificated by  : Hendrik Lanz(modificated functions were marked with #**)
Contact:
    Email       : name42@riseup.net
    GitHub      : pythondealer


"""

from PIL import Image
import subprocess
import os
from getopt import getopt
from sys import argv
from cryptography.fernet import Fernet
import base64
import hashlib



def changeLast2Bits(origByte: int, newBits: int) -> int:
    """
    This function replaces the 2 LSBs of the given origByte with newBits
    """
    # First shift bits to left 2 times
    # Then shift bits to right 2 times, now we lost the last 2 bits
    # Perform OR operation between original_number and new_bits

    return (origByte >> 2) << 2 | newBits


def filesizeToBytes(data: bytes) -> bytes:
    """
    This function returns the size of data in 8 bytes
    """
    return (len(data)).to_bytes(8, byteorder='big')


def serializeData(data: bytes, padding: int = 1) -> list:
    """
    This function packs data into groups of 2bits and returns that list
    """
    serializedData = list()
    for datum in data:
        serializedData.append((datum >> 6) & 0b11)
        serializedData.append((datum >> 4) & 0b11)
        serializedData.append((datum >> 2) & 0b11)
        serializedData.append((datum >> 0) & 0b11)

    while len(serializedData) % padding != 0:
        serializedData.append(0)

    return serializedData


def deserializeData(data: list) -> bytes:
    """
    This function takes data and unpacks the '2bits groups' to get original data back
    """
    deserializeData = list()
    for i in range(0, len(data) - 4 + 1, 4):
        datum = (data[i] << 6) + (data[i + 1] << 4) + (data[i + 2] << 2) + (data[i + 3] << 0)
        deserializeData.append(datum)

    return bytes(deserializeData)


magicBytes = {
    "encryptedLSB": 0x1337c0de,
    "unencryptedLSB": 0xdeadc0de,
    "encrypted": 0xbabec0de,
    "unencrypted": 0x5afec0de
}


def hideDataToImage(inputImagePath: str, fileToHidePath: str, outputImagePath: str, password: str, hidingMode: str) -> None:
    """
    This function hides the fileToHidePath file inside the image located at inputImagePath,
    and saves this modified image to outputImagePath.
    """
    fp = open(fileToHidePath, "rb")

    data = fp.read()
    print("[*] {} file size : {} bytes".format(fileToHidePath, len(data)))

    if hidingMode == "lsb":
        image = Image.open(inputImagePath).convert('RGB')
        pixels = image.load()

        if password:
            data = encryptData(data, password)
            print("[*] Encrypted data size: {} bytes".format(len(data)))
            data = (magicBytes["encryptedLSB"]).to_bytes(4, byteorder='big') + filesizeToBytes(data) + data
            print("[*] Magic bytes used: {}".format(hex(magicBytes["encryptedLSB"])))
        else:
            data = (magicBytes["unencryptedLSB"]).to_bytes(4, byteorder='big') + filesizeToBytes(data) + data
            print("[*] Magic bytes used: {}".format(hex(magicBytes["unencryptedLSB"])))

        if len(data) > (image.size[0] * image.size[1] * 6) // 8:
            print("[*] Maximum hidden file size exceeded")
            print("[*] Maximum hidden file size for this image: {}".format((image.size[0] * image.size[1] * 6) // 8))
            print("[~] To hide this file, choose a bigger resolution")

            size_err = True#**            
            return size_err


        print("[*] Hiding file in image")
        data = serializeData(data, padding=3)
        data.reverse()

        imageX, imageY = 0, 0
        while data:
            # Pixel at index x and y
            pixel_val = pixels[imageX, imageY]

            # Hiding data in all 3 channels of each Pixel
            pixel_val = (changeLast2Bits(pixel_val[0], data.pop()),
                         changeLast2Bits(pixel_val[1], data.pop()),
                         changeLast2Bits(pixel_val[2], data.pop()))

            # Save pixel changes to Image
            pixels[imageX, imageY] = pixel_val

            if imageX == image.size[0] - 1:          # If reached the end of X Axis
                # Increment on Y Axis and reset X Axis
                imageX = 0
                imageY += 1
            else:
                # Increment on X Axis
                imageX += 1

        if not outputImagePath:
            outputImagePath = ".".join(inputImagePath.split(".")[:-1]) + "_with_hidden_file" + "." + inputImagePath.split(".")[-1]

        print(f"[+] Saving image to {outputImagePath}")
        image.save(outputImagePath)
    elif hidingMode == "endian":
        if password:
            data = encryptData(data, password)
            print("[*] Encrypted data size: {} bytes".format(len(data)))
            data = data + filesizeToBytes(data) + (magicBytes["encrypted"]).to_bytes(4, byteorder='big')
            print("[*] Magic bytes used: {}".format(hex(magicBytes["encrypted"])))
        else:
            print("[!] Warning: You should encrypt file if using endian mode")
            data = data + filesizeToBytes(data) + (magicBytes["unencrypted"]).to_bytes(4, byteorder='big')
            print("[*] Magic bytes used: {}".format(hex(magicBytes["unencrypted"])))

        inputImage = open(inputImagePath, "rb").read()
        inputImage += data

        outputImage = open(outputImagePath, "wb")
        outputImage.write(inputImage)
        outputImage.close()



def extractDataFromImage(inputImagePath: str, outputFilePath: str, password: str) -> None:
    """
    This function extracts the hidden file from inputImagePath image and saves it to outputFilePath
    """

    inputImage = open(inputImagePath, "rb").read()
    if int.from_bytes(inputImage[-4:], byteorder='big') in [magicBytes["encrypted"], magicBytes["unencrypted"]]:
        print("[+] Hidden file found in image")
        hiddenDataSize = int.from_bytes(inputImage[-12:-4], byteorder="big")
        hiddenData = inputImage[-hiddenDataSize - 12:-12]

        if int.from_bytes(inputImage[-4:], byteorder='big') == magicBytes["encrypted"]:
            print("[*] Hidden file is encrypted")
            hiddenData = decryptData(hiddenData, password)

        print("[*] Extracting hidden file from image")
        print(f"[+] Saving hidden file to {outputFilePath}")

        outputFilePath = open(outputFilePath, "wb")
        outputFilePath.write(hiddenData)
        outputFilePath.close()

        print(f"[*] Size of hidden file recovered : {len(hiddenData)} bytes")
    else:

        image = Image.open(inputImagePath).convert('RGB')
        pixels = image.load()

        data = list()                                 # List where we will store the extracted bits
        for imageY in range(image.size[1]):
            for imageX in range(image.size[0]):
                if len(data) >= 48:
                    break

                # Read pixel values traversing from [0, 0] to the end
                pixel = pixels[imageX, imageY]

                # Extract hidden message in chunk of 2 bits from each Channel
                data.append(pixel[0] & 0b11)
                data.append(pixel[1] & 0b11)
                data.append(pixel[2] & 0b11)

        encrypted = False
        if deserializeData(data)[:4] == bytes.fromhex(hex(magicBytes["unencryptedLSB"])[2:]):
            print("[+] Hidden file found in image")
        elif deserializeData(data)[:4] == bytes.fromhex(hex(magicBytes["encryptedLSB"])[2:]):
            print("[*] Hidden file is encrypted")
            encrypted = True
        else:
            print("[!] Image don't have any hidden file")
            print("[*] Magic bytes found:    0x{}".format(deserializeData(data)[:4].hex()))
            print("[*] Magic bytes supported: {}".format(", ".join([hex(x) for x in magicBytes.values()])))
            exit()

        print("[*] Extracting hidden file from image")
        hiddenDataSize = int.from_bytes(deserializeData(data)[4:16], byteorder='big') * 4

        data = list()
        for imageY in range(image.size[1]):
            for imageX in range(image.size[0]):
                if len(data) >= hiddenDataSize + 48:
                    break

                # Read pixel values traversing from [0, 0] to the end
                pixel = pixels[imageX, imageY]

                # Extract hidden message in chunk of 2 bits from each Channel
                data.append(pixel[0] & 0b11)
                data.append(pixel[1] & 0b11)
                data.append(pixel[2] & 0b11)

        data = deserializeData(data[48:])
        if encrypted:
            pw_err = False
            data = decryptData(data, password)

        if data == ("[!] Invalid password or data"):
            pw_err = True
            return pw_err

        if pw_err == False:
        
            print(f"[+] Saving hidden file to {outputFilePath}")
            print(f"[*] Size of hidden file recovered : {len(data)} bytes")

            f = open(outputFilePath, 'wb')
            f.write(data)
            f.close()


def remove_from_drive(fileToHidePath):#**

    # check if drive is SSD or HDD by checking if the drive is rotating
    disk_type = ("")

    disk_type = subprocess.check_output(["cat", "/sys/block/sda/queue/rotational"])

    disk_type = disk_type.decode()
    disk_type = disk_type.replace("\n", "")
    print(disk_type)

    # if drive is SSD "disk_type" will be 0
    if disk_type == "0": 


        misc_to_overwrite = ("sjkdhfskathjeazhu34tq25gaszhgwkah534")
        zeros_for_overwriting = ("00000000000000000000000000000000000000000000")
        rounds = 0

        while rounds <= 2:#  Loop for overwriting the file multiple times

            f = open(fileToHidePath, 'w+')
            f.write(misc_to_overwrite)
            f.close()

            f = open(fileToHidePath, 'w+')
            f.write(zeros_for_overwriting)
            f.close()
            rounds += 1
            
        os.remove(fileToHidePath)
        print("removed")


    # if drive is HDD "disk_type" will be 1
    if disk_type == 1:
        delete = subprocess.run(["shred", "-uz", fileToHidePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        

def encryptData(data: bytes, key: str) -> bytes:
    key = base64.urlsafe_b64encode(hashlib.md5(key.encode()).hexdigest().encode())

    f = Fernet(key)
    encData = f.encrypt(data)
    return encData

def decryptData(data: bytes, key: str) -> bytes:

    try:
        key = base64.urlsafe_b64encode(hashlib.md5(key.encode()).hexdigest().encode())

        f = Fernet(key)
        decData = f.decrypt(data)
        return decData
    except:
        print("[!] Invalid password or data")
        pw_err_msg = ("[!] Invalid password or data")
        return pw_err_msg





