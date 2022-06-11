import sys
import __init__ as archive
if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        print("Enter a argument")
    for i in sys.argv[1:]:
        if i == "-v":
            print(archive.ARCHIVE_VERSION)
            sys.exit(0)
        if i == "-c":
            try:
                location = sys.argv[sys.argv.index("-c")+1]
                name = sys.argv[sys.argv.index("-c")+2]
            except IndexError:
                print("-c requires two arguments\n\tLocation\n\tName")
                sys.exit(1)
            archive.create(location,name)
            sys.exit(0)
        elif i == "-a":
            try:
                location = sys.argv[sys.argv.index("-a")+1]
                name = sys.argv[sys.argv.index("-a")+2]
                data = open(sys.argv[sys.argv.index("-a")+3],"rb").read()
                data = data.hex()
            except IndexError:
                print("-a requires three arguments\n\tLocation\n\tName\n\tData")
                sys.exit(1)
            archive.add(location,name,data)
        elif i == "-l":
            try:
                location = sys.argv[sys.argv.index("-l")+1]
            except IndexError:
                print("-l requires one argument\n\tLocation")
                sys.exit(1)
            for i in archive.ls(location):
                print(i)
            sys.exit(0)
        elif i == "-g":
            try:
                location = sys.argv[sys.argv.index("-g")+1]
                name = sys.argv[sys.argv.index("-g")+2]
            except IndexError:
                print("-g requires two arguments\n\tLocation\n\tName")
                sys.exit(1)
            print(archive.get.data(location,name))
            sys.exit(0)
        elif i == "-e":
            try:
                location = sys.argv[sys.argv.index("-e")+1]
                name = sys.argv[sys.argv.index("-e")+2]
                destination = sys.argv[sys.argv.index("-e")+3]
            except IndexError:
                print("-e requires three arguments\n\tLocation\n\tName\n\tDestination")
                sys.exit(1)
            data = archive.get.data(location,name)
            with open(destination,"wb") as f:
                try:
                    f.write(bytes.fromhex(data))
                except ValueError:
                    print("Could not extract the file from the archive. The file may be corrupt or the archive version is old or too new.")
        elif i == "-r":
            try:
                location = sys.argv[sys.argv.index("-r")+1]
                name = sys.argv[sys.argv.index("-r")+2]
            except IndexError:
                print("-r requires two arguments\n\tLocation\n\tName")
                sys.exit(1)
            archive.remove(location,name)
            sys.exit(0)
        elif i == "-R":
            try:
                location = sys.argv[sys.argv.index("-R")+1]
                name = sys.argv[sys.argv.index("-R")+2]
                newname = sys.argv[sys.argv.index("-R")+3]
            except IndexError:
                print("-R requires three arguments\n\tLocation\n\tName\n\tNew Name")
                sys.exit(1)
            archive.rename(location,name,newname)
            sys.exit(0)
        else:
            print("Enter a valid command")