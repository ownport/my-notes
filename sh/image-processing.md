# Image processing

The [identify](http://www.imagemagick.org/script/identify.php) program describes the format and characteristics of one or more image files. It also reports if an image is incomplete or corrupt. The information returned includes the image number, the file name, the width and height of the image, whether the image is colormapped or not, the number of colors in the image, the number of bytes in the image, the format of the image (JPEG, PNM, etc.), and finally the number of seconds it took to read and process the image. Many more attributes are available with the verbose option. 

```
$ identify rose.jpg
rose.jpg JPEG 640x480 sRGB 87kb 0.050u 0:01
```

