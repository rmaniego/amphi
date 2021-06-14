"""
    Studio
    MoviePy Wrapper
    (c) 2021
"""

import os

from vidstab import VidStab
from sometime import Sometime
from moviepy.editor import AudioFileClip, VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips

def strip_filename(path):
    path = path.replace("\\", "/")
    return list(path.split("/"))[-1]

class Amphi:
    def __init__(self, width=1080):
        self.width = 1080
        if isinstance(width, int):
            self.width = width

        self.height = int((self.width * 9 / 16))
        self.dimension = self.width, self.height

        self.clips = []
        self.audios = {}
        self.videos = {}
        self.texts = {}
        self.audio_clip = None
        self.video_clip = None
        self.video_clip_name = None
        
        if not os.path.exists("studio/stabilized"):
            os.makedirs("studio/stabilized")
    
    def new_audio(self, name, path):
        try:
            self.audios.update({name: AudioFileClip(path)})
        except:
            pass
        return self
    
    def new_video(self, name, path, stabilize=False):
        try:
            if stabilize:
                filename = strip_filename(path)
                stablized = f"media/stabilized/{filename}"
                if not os.path.exists(stablized):
                    stabilizer = VidStab()
                    stabilizer.stabilize(input_path=path, output_path=stablized, border_type="reflect")
                path = stablized
            self.videos.update({name: VideoFileClip(path)})
        except:
            pass
        return self
    
    def video(self, name):
        self.video_clip_name = name
        self.video_clip = self.videos.get(name, None)
        return self
    
    def new_text(self, name, data, color="white", font="Arial", kerning=5, fontsize=12, position="center", duration=10):
        try:
            clip = TextClip(data, color=color, font=font, kerning=kerning, fontsize=fontsize)
            clip = clip.set_pos(position).set_duration(duration)
            self.texts.update({name: clip})
        except:
            pass
        return self
    
    def subclip(self, start, end=None):
        if self.video_clip is not None:
            if end is None:
                end = self.video_clip.duration
            duration = end - start
            if duration > 5:
                max_duration = min((start+5), self.video_clip.duration)
                end = start + max_duration
            self.video_clip = self.video_clip.subclip(start, end)
        return self
    
    def resize_width(self, width=0):
        if self.video_clip is not None:
            if not isinstance(width, int):
                width = self.width
            if width < 1:
                width = self.width
            self.resize(width=width)
    
    def resize_height(self, height=0):
        if self.video_clip is not None:
            if not isinstance(height, int):
                height = self.height
            if height < 1:
                height = self.height
            self.resize(height=height)
    
    def keep(self, name):
        if self.video_clip is not None:
            self.videos.update({name: self.video_clip})
        return self
            
    
    def composite(self, name):
        if self.video_clip is not None:
            clip = self.texts.get(name, None)
            if clip is not None:
                self.video_clip = CompositeVideoClip([self.video_clip, clip])
        return self
    
    def concatenate(self, name):
        if self.video_clip is not None:
            clip = self.videos.get(name, None)
            if clip is not None:
                self.video_clip = concatenate_videoclips([self.video_clip, clip])
        return self
    
    def concatenate_by_video_id(self, names):
        if isinstance(names, list):
            clips = []
            for name in names:
                clip = self.videos.get(name, None)
                if clip is not None:
                    clips.append(clip)
            if len(clips) > 0:
                self.video_clip = concatenate_videoclips(clips)
        return self
    
    def set_audio(self, name):
        if self.video_clip is not None:
            audio = self.audios.get(name, None)
            if audio is not None:
                self.video_clip = self.video_clip.set_audio(audio)
        return self
    
    def fadein(self, duration):
        if self.video_clip is not None:
            try:
                if duration > 0:
                    self.video_clip.fadein(float(duration))
            except:
                pass
        return self
    
    def fadeout(self, duration):
        if self.video_clip is not None:
            try:
                if duration > 0:
                    self.video_clip.fadeout(float(duration))
            except:
                pass
        return self
    
    def render(self, index=-1):
        if self.video_clip is not None:
            try:
                if 0 <= index < len(self.clips):
                    self.clips.insert(index, self.video_clip)
                else:
                    self.clips.append(self.video_clip)
            except:
                pass
            self.video_clip = None
            self.video_clip_name = None
        return self

    def save(self, filename, fps=24, audio_bitrate="256k", bitrate="8000k", codec="mpeg4"):
        if len(self.clips) > 0:
            video = concatenate_videoclips(self.clips)
            video.write_videofile(filename, fps=fps, audio_bitrate=audio_bitrate, bitrate=bitrate, codec=codec)
            return True
        return False