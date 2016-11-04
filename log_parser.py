import os

def parse(file):
    try:
        with open(file, "r") as f:
            for line in f.readlines():
                print line
    except Exception as e:
        print e
    finally:
        f.close()

parse(os.path.join("/Users/uday/Documents/logs", "uday.log"))
