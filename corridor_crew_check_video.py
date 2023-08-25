#!/usr/bin/python

import os
import re
import sys
import glob

try:
    import ffmpeg
except ImportError:
    print("Maybe you are missing the library?\ntry \"pip install ffmpeg-python\"")
    exit(1)

# Original video data
# Video-ID, duration, frame-count
metadata_list = [
    ["V1-0001","2.127125","51"],
    ["V1-0002","1.209542","29"],
    ["V1-0003","2.377375","57"],
    ["V1-0004","2.794458","67"],
    ["V1-0005","2.502500","60"],
    ["V1-0006","1.459792","35"],
    ["V1-0007","2.377375","57"],
    ["V1-0008","4.421083","106"],
    ["V1-0009","2.293958","55"],
    ["V1-0010","1.876875","45"],
    ["V1-0011","3.253250","78"],
    ["V1-0012","2.210542","53"],
    ["V1-0013","3.294958","79"],
    ["V1-0014","2.752750","66"],
    ["V1-0015","1.710042","41"],
    ["V1-0016","1.793458","43"],
    ["V1-0017","1.001000","24"],
    ["V1-0018","2.085417","50"],
    ["V1-0019","2.168833","52"],
    ["V1-0020","1.793458","43"],
    ["V1-0021","1.418083","34"],
    ["V1-0022","1.084417","26"],
    ["V1-0023","1.543208","37"],
    ["V1-0024","0.834167","20"],
    ["V1-0025","3.086417","74"],
    ["V1-0026","1.584917","38"],
    ["V1-0027","0.834167","20"],
    ["V1-0028","0.917583","22"],
    ["V1-0029","2.335667","56"],
    ["V1-0030","2.252250","54"],
    ["V1-0031","1.167833","28"],
    ["V1-0032","2.127125","51"],
    ["V1-0033","3.753750","90"],
    ["V1-0034","3.628625","87"],
    ["V1-0035","2.502500","60"],
    ["V1-0037","1.626625","39"],
    ["V1-0038","6.131125","147"],
    ["V1-0039","2.127125","51"],
    ["V1-0040","2.502500","60"],
    ["V1-0041","2.377375","57"],
    ["V1-0042","3.670333","88"],
    ["V1-0043","1.543208","37"],
    ["V1-0044","1.584917","38"],
    ["V1-0045","1.042708","25"],
    ["V1-0046","3.795458","91"],
    ["V1-0047","1.543208","37"],
    ["V1-0048","3.503500","84"],
    ["V1-0049","2.752750","66"],
    ["V1-0050","1.292958","31"],
    ["V1-0051","1.376375","33"],
    ["V1-0052","2.836167","68"],
    ["V1-0053","2.210542","53"],
    ["V1-0054","4.546208","109"],
    ["V1-0055","3.128125","75"],
    ["V1-0056","1.292958","31"],
    ["V1-0057","1.084417","26"],
    ["V1-0058","5.422083","130"],
    ["V1-0059","2.043708","49"],
    ["V1-0060","1.543208","37"],
    ["V1-0061","2.711042","65"],
    ["V1-0062","2.961292","71"],
    ["V1-0063","2.252250","54"],
    ["V1-0064","4.879875","117"],
    ["V1-0065","4.921583","118"],
    ["V1-0066","3.545208","85"],
    ["V1-0067","2.127125","51"],
    ["V1-0068","1.960292","47"],
    ["V1-0069","4.295958","103"],
    ["V1-0070","2.293958","55"],
    ["V1-0071","2.127125","51"],
    ["V1-0072","3.378375","81"],
    ["V1-0073","2.293958","55"],
    ["V1-0074","2.335667","56"],
    ["V1-0075","2.335667","56"],
    ["V1-0076","1.126125","27"],
    ["V1-0077","2.002000","48"],
    ["V1-0078","2.168833","52"],
    ["V1-0079","1.251250","30"],
    ["V1-0080","1.793458","43"],
    ["V1-0081","2.168833","52"],
    ["V1-0082","2.127125","51"],
    ["V1-0083","2.961292","71"],
    ["V1-0084","3.461792","83"]
]

def check(file_path):
    # Check naming
    basename = os.path.basename(file_path)
    print("Checking " + file_path)

    r1 = re.compile("(V1-00\d\d)_Anime_Baseball_Challenge_Renders_(.+)\\.mp4")
    m = r1.match(basename)

    if not m:
        print("Error, ops!")
        print("The name of your file does not match the pattern.")
        print("It needs to be V1-00xx_Anime_Baseball_Challenge_Renders_YOURNAMEHERE.mp4")
        return False

    video_id, yourname = m.groups()

    print("Video ID: " + video_id)

    meta_entry = None
    for metadata in metadata_list:
        if metadata[0] == video_id:
            meta_entry = metadata
            break

    if not meta_entry:
        print("Error, ops!")
        print("Video ID not found in the list!")
        for metadata in metadata_list:
            print(metadata)
        return False

    print("Your name: " + yourname)

    streams = ffmpeg.probe(file_path)["streams"]

    stream = streams[0]

    r_frame_rate = stream["r_frame_rate"]
    nb_frames = stream["nb_frames"]
    codec_name = stream["codec_name"]
    duration = stream["duration"]
    width = stream["width"]
    height = stream["height"]

    if codec_name != "h264":
        print("Error, ops!")
        print("ffmpeg probe")
        print(stream)
        print("Codec name different from h264!")
        return False
        
    if r_frame_rate != "24000/1001":
        print("Error, ops!")
        print("ffmpeg probe")
        print(stream)
        print("Your frame rate needs to be 24000/1001, currently is " + r_frame_rate)
        return False

    if width != 1920 or height != 1080:
        print("Error, ops!")
        print("ffmpeg probe")
        print(stream)
        print("Resolution needs to be 1920x1080!")
        return False

    if nb_frames != meta_entry[2]:
        print("Error, ops!")
        print("ffmpeg probe")
        print(stream)
        print("Number of frames does not match original video!")
        print("It should be " + meta_entry[2])
        return False

    if duration != meta_entry[1]:
        print("Error, ops!")
        print("ffmpeg probe")
        print(stream)
        print("Durating does not match original video!")
        print("It should be " + meta_entry[1])
        return False
    
    if len(streams) != 1:
        print("There are multiple streams on this video, the video should not have audio!")
        return False
    print("File " + file_path + " OK!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} path/to/you/file/or/directory".format(os.path.basename(sys.argv[0])))
        exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("Error, ops!")
        print("Path does not exist!")
        exit(1)

    if os.path.isfile(file_path):
        files = [file_path]

    if os.path.isdir(file_path):
        print("Searching all mp4 files in " + file_path)
        files = glob.glob(file_path + os.sep + '**' + os.sep + '*.mp4', recursive = True)

    ok = []
    nok = []
    for f in files:
        result_ok = check(f)
        print("----")
        if result_ok:
            ok.append(f)
        else:
            nok.append(f)
    
    print("OK videos")
    print("---------")
    for f in ok:
        print(f)

    print("Not OK videos")
    print("-------------")
    for f in nok:
        print(f)
