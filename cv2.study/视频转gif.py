from moviepy.editor import VideoFileClip

def video_to_gif(input_video, output_gif, fps):
    video = VideoFileClip(input_video)
    video.write_gif(output_gif, fps=fps)

# 设置输入视频路径、输出GIF路径和帧率
input_video_path = "ppp.mp4"
output_gif_path = "output_animation.gif"
gif_fps = 10

# 调用函数进行转换
video_to_gif(input_video_path, output_gif_path, gif_fps)
