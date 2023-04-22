import os
from pydub import AudioSegment
from moviepy.editor import * 


def createAudio():
    audio = AudioSegment.from_file("audio.wav", format="wav")

    octaves = 0.5
    new_sample_rate = int(audio.frame_rate * (2.0 ** octaves))

    output_sound = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
    output_sound = output_sound.set_frame_rate(44100)

    output_sound = output_sound[30 * 1000:]

    
    output_sound.export("out.wav", format="wav")

def createVideo():
    path = "./poze"
    dir_list = os.listdir(path)

    intro = VideoFileClip("./intro.gif").resize(width=800)
    pictures = [ImageClip(f"{path}/{picture_path}").set_duration(2).resize(width=800).fx(vfx.fadein, 0.3) for picture_path in dir_list]

    audio_clip = AudioFileClip("out.wav")
    audio_clip = audio_clip.audio_fadein(3)

    video_clip = concatenate([intro] + pictures, method="compose")
    
    audio_clip = audio_clip.subclip(0, video_clip.end)
    video_clip.audio = CompositeAudioClip([audio_clip])
    video_clip.write_videofile('test.mp4', fps=24)

createAudio()
createVideo()
