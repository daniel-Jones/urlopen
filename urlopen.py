#!/usr/bin/env python2.7
import sys, os;
from urlparse import urlparse;
def run(process, arg):
    L = [];
    for each in process:
        L.append(each);
    L.append(arg);
    os.spawnvpe(os.P_NOWAIT, L[0], L, os.environ)

def main(args):
    images = ["jpg", "png"]; imageapp = ["feh"];
    videos = ["gif", "gifv", "webm", "mp4"]; videoapp = ["mpv", "--loop"];
    videourls = ["youtube.com", "youtu.be", "streamable.com"];
    pdf = ["pdf"]; pdfapp = ["mupdf"];
    defaultapp = ["/home/daniel_j/compiled/waterfox/waterfox"];
    defaultforcedurls = ["slack.com"];
    x = 0;
    for each in args:
        parsed_uri = urlparse(each);
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri);
        if (any (s in domain for s in defaultforcedurls)):
                print("running with forced default application {}".format(each));
                run(defaultapp, each);
        elif (each.lower().endswith(tuple(images))):
                print("image {}".format(each));
                run(imageapp, each);
        elif (each.lower().endswith(tuple(videos))):
                print("video {}".format(each));
                run(videoapp, each);
        elif (each.lower().endswith(tuple(pdf))):
                print("pdf {}".format(each));
                run(pdfapp, each);
        elif (any(s in domain for s in videourls)):
                print("video {}".format(each));
                run(videoapp, each);
        else:
            print("running with default application {}".format(each));
            run(defaultapp, each);
        x += 1;

if __name__ == "__main__":
    if sys.argv > 1:
        main(sys.argv[1:]);
