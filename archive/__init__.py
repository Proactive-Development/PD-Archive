ARCHIVE_VERSION = "1.0"
class identifiers:
    METADATA_START = "00Ae7YFrOimIFtXROgvieYMSypCPWC00"
    METADATA_END = "00exDPOAQ2RZP3qnpo6gXOVWKg6pKf00"
    DATA_START = "00vt4QldTXcuFcwt6ZOU3rJNFLCfNg00"
    DATA_END = "00xFes3PMUW4DaNmBkKqY4qfxvoCLn00"
    class metadata:
        name = "00NAME00"
        data = "00DATA00"
        archive_version = "00VERSION00"+ARCHIVE_VERSION
def create(location,name):
    file = ""
    with open(location,"w") as f:
        file += identifiers.METADATA_START
        file += identifiers.metadata.name+name
        file += identifiers.metadata.archive_version
        file += identifiers.METADATA_END
        f.write(file)

def add(location,name,data):
    with open(location,"r") as f:
        file = f.read()
    file += identifiers.DATA_START
    file += identifiers.metadata.name+name
    file += identifiers.metadata.data+data
    file += identifiers.DATA_END
    with open(location,"w") as f:
        f.write(file)
def ls(location):
    with open(location,"r") as f:
        file = f.read()
    f = file.split(identifiers.METADATA_END)[-1]
    f = file.split(identifiers.DATA_START)[1:]
    out = []
    for i in f:
        out.append(i.split(identifiers.metadata.name)[-1].split(identifiers.metadata.data)[0])
    return out
class get:
    def data(location,name):
        with open(location,"r") as f:
            file = f.read()
        f = file.split(identifiers.METADATA_END)[-1]
        f = file.split(identifiers.DATA_START)[1:]
        for i in f:
            if i.split(identifiers.metadata.name)[-1].split(identifiers.metadata.data)[0] == name:
                return i.split(identifiers.metadata.data)[-1].replace(identifiers.DATA_END,"")
        raise FileNotFoundError("The file was not found inside the archive")
def remove(location,name):
    with open(location,"r") as f:
        file = f.read()
    file = file.replace(identifiers.DATA_START+identifiers.metadata.name+name+identifiers.metadata.data+get.data(location=location,name=name)+identifiers.DATA_END,"")
    with open(location,"w") as f:
        f.write(file)
def rename(location,name,newname):
    with open(location,"r") as f:
        file = f.read()
    file = file.replace(identifiers.DATA_START+identifiers.metadata.name+name+identifiers.metadata.data+get.data(location=location,name=name)+identifiers.DATA_END,identifiers.DATA_START+identifiers.metadata.name+newname+identifiers.metadata.data+get(location=location,name=name)+identifiers.DATA_END)
    with open(location,"w") as f:
        f.write(file)