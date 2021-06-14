# amphi
MoviePy OOP wrapper

## Additional Requirements
 - ImageMagick binary file

## Usage
```python
from amphi import Amphi

movie = Amphi()

movie.new_audio("music", "<path/to/audio/file>")
movie.new_video("video1", "<path/to/audio/file>")
movie.new_video("video2", "<path/to/audio/file>")
movie.new_video("video3", "<path/to/audio/file>", stabilize=True)
movie.new_text("title", "My Video", font="Arial", fontsize=100, duration=4)



print("Processing media resources...")
movie.video("video1").subclip(0, 5).keep("video1a")
movie.video("video2").subclip(0, 2).keep("video2a")
movie.video("video3").subclip(2).keep("video3a")

movie.video("video1a").composite("title").keep("intro")
movie.concatenate_by_video_id(["intro", "video2a", "video3a"])
movie.set_audio("music")
movie.render()

if movie.save("my-movie.mp4", fps=30, bitrate="16000k"):
    print("The video has been successfully saved.")

```


