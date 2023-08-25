# Corridor Crew Challenge Tools

## corridor_crew_check_video.py

### How to install:
``pip install ffmpeg-python``

### How to run:

for one video

``python corridor_crew_check_video.py "file.mp4"``

or for a folder (it finds videos recursive)

``python corridor_crew_check_video.py "relative-or-full-path\folder-with-mp4s\"``

### What does it check?

- If the file name matches V1-00xx_Anime_Baseball_Challenge_Renders_TEXTHERE.mp4
- If your video has only one stream inside the file (no audio)
- If the resolution of your video is 1920x1080
- If the frame rate is 24000/1001 which is 23.976
- Codec h.264
- If the duration of your video matches the duration of the original video
- If the number of frames matches the number of frames of the original video

### Specs (from discord FAQ)

Frame rate: 23.976
Resolution: 1920x1080

Format: mp4

Codec: h.264

NO AUDIO TRACKS

File Name: The file submitted should be the exact same file name as the file you downloaded with an "_ARTISTNAME" added to the end of the file.
For example, shot  "V1-0002_Anime_Baseball_Challenge_Renders" would be submitted as V1-0002_Anime_Baseball_Challenge_Renders_JONAH".
Simply add your name to the end of the file and you are all set! Any files that deviate from that naming convention will not be considered, so please adhere to this exactly.
