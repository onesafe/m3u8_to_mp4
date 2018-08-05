# m3u8_to_mp4
convert m3u8 to mp4

用法：`python convert_m3u8_to_mp4.py m3u8文件 目标mp4文件名`


思路：m3u8文件里面会包含很多的ts文件，首先将这些ts文件下载下来，这些ts文件是可以直接用播放器播放的，但是都是十秒左右的小视频文件，将这些ts文件合并成一个mp4文件就可以了


* 打开 m3u8
* 下载m3u8里面的ts文件
* 合并ts文件为mp4文件
