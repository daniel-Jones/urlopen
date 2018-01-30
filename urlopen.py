#!/usr/bin/env python2.7
import sys, os;

def run(process, arg):
    L = [];
    for each in process:
        L.append(each);
    L.append(arg);
    os.spawnvpe(os.P_NOWAIT, L[0], L, os.environ)

def main(args):
    images = ["jpg", "png"]; imageapp = ["feh"];
    videos = ["gif", "webm", "mp4"]; videoapp = ["mpv", "--loop"];
    pdf = ["pdf"]; pdfapp = ["mupdf"];
    defaultapp = ["/home/daniel_j/compiled/waterfox/waterfox"];
    x = 0;
    for each in args:
        if (each.endswith(tuple(images))):
                print("image {}".format(each));
                run(imageapp, each);
        elif (each.endswith(tuple(videos))):
                print("video {}".format(each));
                run(videoapp, each);
        elif (each.endswith(tuple(pdf))):
                print("pdf {}".format(each));
                run(pdfapp, each);
        else:
            print("running with default application {}".format(each));
            run(defaultapp, each);
        x += 1;

if __name__ == "__main__":
    if sys.argv > 0:
        main(sys.argv[1:]);
