import sys
import os
from PIL import Image

print("\n Extract the TIFF Image Properties: \n    Dimension\n    Format\n    Color Mode\n    Resolution (DPI)\n    Compression\n    File Size")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 27 May 2022 \n\n")

filepath1 = input(" Enter the File path: ")

filepath = filepath1 + "\\"

filelist = os.path.isdir(filepath)

if os.path.exists(filepath + 'output.txt'):                                                    # remove the 'output.txt' file if already present in the folder
    os.remove(filepath + 'output.txt')


for fname in os.listdir(filepath):
    if not fname.endswith(".tif"):
        continue
    path = os.path.join(filepath, fname) 
    print(path)
    img = Image.open(path)    
    dimension = fname + " " + "Width & Height: " + str(img.size) + "\n"                        # for getting Image Width & Height
    img_format = fname + " " + "Format: " + str(img.format) + "\n"                             # for getting Image Format
    img_mode = fname + " " + "Mode: " + str(img.mode) + "\n"                                   # for getting Image Color Mode RGB, 
    img_dpi = fname + " " + "Resolution: " + str(img.info['dpi']) + "\n"                       # for getting Image DPI
    img_compr = fname + " " + "Compression: " + str(img.info['compression']) + "\n"            # for getting Image Compression Mode (raw means "no compression), tiff_lzw, group4    
    filesize = os.path.getsize(path)                                                           # for getting Image file size (in bytes)
    size_mb = str(round(os.path.getsize(path)/1024/1024, 2))                                   # Image file size (bytes to mb)
    img_size =  fname + " " + "File Size: " + str(filesize) + " bytes" + " (" + size_mb + " MB)" + "\n\n"
    text_file = filepath + "output.txt"    
    f = open(text_file, "a+")                                                                  # "a+" means appending the all image properties one by one 
    f.write(str(dimension))                                                                    # writing all properties one by one to output text file
    f.write(str(img_format))
    f.write(str(img_mode))
    f.write(str(img_dpi))
    f.write(str(img_compr))
    f.write(str(img_size))
    f.close()
print("Completed")





