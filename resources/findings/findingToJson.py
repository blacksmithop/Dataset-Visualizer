from os import listdir, path, remove
from json import dump, load
from re import sub

dir = "./resources/findings/json"  # directory where data is to be stored


def createJSON(fileName=None):
    if not fileName:
        fileName = input("> Title: ")

    if not fileName:
        print("[INFO] Skipped file creation")
        return

    titleName = fileName.lower().split()

    jsonName = "_".join(titleName)

    dataDict = {
        "subject": "",
        "data": {"description": "", "keywords": []},
    }

    sanitizedName = sub("[^A-Za-z0-9]+", "", jsonName)

    filePath = f"{dir}/{sanitizedName}.json"

    if not path.exists(filePath):
        with open(filePath, "w") as fp:
            dump(dataDict, fp, indent=4)
            print(f"[INFO] Created file at {filePath}")


def combineJSON():
    combinedDict = []
    for file in listdir(dir):
        with open(path.join(dir, file), "r") as fp:
            combinedDict.append(load(fp))

    _fileName = path.join("./resources/findings/", "full-data.json")
    if path.exists(_fileName):
        try:
            remove(_fileName)
        except OSError as e:
            print(e.strerror)

    with open(_fileName, "w") as fp:
        dump(combinedDict, fp, indent=4)


if __name__ == "__main__":

    try:
        createJSON()
    except KeyboardInterrupt:
        exit(0)

    print("[INFO] Compiling data to file full-data.json")
    combineJSON()
