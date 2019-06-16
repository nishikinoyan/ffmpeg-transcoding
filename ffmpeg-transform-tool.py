import os
import subprocess
import threading
import time
from delete_file import *

class FFmpeg_Transform():
    __video_format = ['mp4','avi','mkv']
    __audio_format = ['mp3','wav','flac']
    def __init__(self):
        ffmpeg_check = subprocess.getstatusoutput('ffmpeg')
        if ffmpeg_check[1][0:6] != 'ffmpeg':
            print('ffmpeg 未安装')
        else:
            print('ffmpeg 已安装')
    def video_transcoding(self,input_path,out_path,video_rate,video_size,frame_number,audio_rate,audio_sampling_rate,out_format):
        #ffmpeg - i test.mkv - b 5000 k - s 1920 * 1080 - r 60 - ab 192 k - ar 44100 test.mp4
        global width
        global height
        try:
            width = video_size[0]
            height = video_size[1]
        except Exception as e:
            print('数值错误：' + str(e))
        ffmpeg_shell = 'ffmpeg -i {} -b {}k -s {}*{} -r {} -ab {}k -ar {} {}'
        input_file_name = os.path.basename(os.path.splitext(input_path)[0])
        output_file_name = input_file_name + '_' + str(width) + "×" + str(height) + '_' + str(video_rate) + 'K_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.' + self.__video_format[out_format]
        out_path = os.path.join(out_path,output_file_name)
        if os.path.exists(out_path):
            dir_delete(out_path)
        return_shell = subprocess.getstatusoutput(ffmpeg_shell.format(input_path,video_rate,width,height,frame_number,audio_rate,audio_sampling_rate,out_path))
        return return_shell,out_path

    def audio_transcoding(self,input_path,out_path,audio_rate,audio_sampling_rate,out_format):
        #ffmpeg -i test.mp3 -ab 128k -ar 44100 test2.mp3
        ffmpeg_shell = 'ffmpeg -i {} -ab {}k -ar {} {}'
        input_file_name = os.path.basename(os.path.splitext(input_path)[0])
        out_file_name = input_file_name + '_' + str(audio_rate) + 'k_' + str(audio_sampling_rate) + 'HZ_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.' + self.__audio_format[out_format]
        out_path = os.path.join(out_path,out_file_name)
        if os.path.exists(out_path):
            dir_delete(out_path)
        print(ffmpeg_shell.format(input_path,audio_rate,audio_sampling_rate,out_path))
        return_shell = subprocess.getstatusoutput(ffmpeg_shell.format(input_path,audio_rate,audio_sampling_rate,out_path))
        return return_shell,out_path



if __name__ == '__main__':
    '''
    ffmpeg.video_transcoding(原视频文件路径, '输出路径', 视频码率, 视频尺寸，例：(1280, 720), 视频帧数, 音频比特率, 音频采样率, 格式0,1,2)
    0 -> mp4 ; 1 - > avi ; 2 - > mkv
    '''
    ffmpeg = FFmpeg_Transform()

    cmd,path = ffmpeg.video_transcoding('G:/test\H-test/test.mp4','G:/test\H-test',1000,(1280,720),25,128,44100,0)
    #cmd = ffmpeg.audio_transcoding('G:/test/test.mp3','G:/test',320,44100,2)
    print(cmd)

