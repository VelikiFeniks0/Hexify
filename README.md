# Hexify
Hexify is a simple and tiny CLI tool that converts image pixels into raw bytes.
It's used for [file hex viewer](https://github.com/VelikiFeniks0/file-hex-viewer) to display images on it.

## How to use:
   open your terminal, and type "python hexify.py" and as arguments put your image path, and your binary file path where the image's bytes would be written.
   and the last argument is for displaying the bytes, if you want to display them, type "y", if not, then "n".


Example:
```
$ python ./hexify/hexify.py /user/home/image.png /user/home/result.bin y
```

example.bin is an example of visualization of binary numbers up to 256.
