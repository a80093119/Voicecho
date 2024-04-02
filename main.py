# import pandas as pd 
# ## transform common voice corpus to coresponding data type
# train = pd.read_csv('./cv-corpus-17.0-2024-03-15-zh-TW/cv-corpus-17.0-2024-03-15/zh-TW/train.tsv', sep='\t')
# train["path"] = train["path"].apply(lambda x: x[:-4])
# train2txt = train[["path", "sentence"]].to_csv('./cv-corpus-17.0-2024-03-15-zh-TW/cv-corpus-17.0-2024-03-15/zh-TW/train.txt', sep='\t', index=False, header=None)

## convert .mp3 to .wav
from os import path
import pandas as pd
from os import listdir
import shutil

def mp3towav(src=None, dst=None, srcfolder=None, dstfolder = None):
    import subprocess
    if srcfolder != None and dstfolder != None:
        onlyfiles = [f for f in listdir(srcfolder)]

        for filename in onlyfiles:
            src = srcfolder + filename
            dst = dstfolder + filename[:-4] + ".wav"
            subprocess.call(['ffmpeg', '-i', src, dst])
    elif src != None and dst != None:
        subprocess.call(['ffmpeg', '-i', src, dst])
    else:
        assert "Please input src&dst or filefolder"

## move file into other folder
def copyfile(listname, srcfolder, dstfolder):
    onlyfiles = [f for f in listdir(srcfolder)]
    count = 0
    for filename in onlyfiles:
        if filename[:-4] in listname:
            shutil.copy(srcfolder + filename, dstfolder + filename)
            count += 1
            print(count)
    print('count:', count)

if __name__ == "__main__":
    # mp3towav(srcfolder="D:/Github/Voicecho\data/cv-corpus-17.0-2024-03-15-zh-TW/cv-corpus-17.0-2024-03-15/zh-TW/zh-TW/clips/",
    #          dstfolder="D:/Github/Voicecho\data/cv-corpus-17.0-2024-03-15-zh-TW/cv-corpus-17.0-2024-03-15/zh-TW/zh-TW/train/")
    
    dstfile = pd.read_csv('./data/aidatatang_200zh/transcript/aidatatang_200_zh_transcript.txt', sep='\t', header=None)
    listname = dstfile[0].to_list()
    copyfile(listname, "D:/Github/Voicecho/data/aidatatang_200zh/corpus/train_taiwanfull/G0013/",
             "D:/Github/Voicecho/data/aidatatang_200zh/corpus/train/G0013/")