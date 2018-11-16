import glob
import sys,os



def _get(a):
    if a<10:
        return '000'+str(a)
    elif a<100:
        return '00'+str(a)
    elif a<1000:
        return '0'+str(a)
    elif a<10000:
        return ''+str(a)

dir_ = "/media/mo/Data4/wiki/extracted_files/"

folders = [x[0] for x in os.walk(dir_)]

words = 'new york big apple los angeles san francisco london manchester leeds'.split(" ")


out = open('/home/mo/word2vec_test/0000.txt','w')
counter = 0
name = 0

for folder_ in folders:
    files_ = glob.glob(folder_+'/wiki_*')
    for file_ in files_:
        f = open(file_)

        for line in f:
            flag = 0
            line = line.lower()
            for w in words:
                if ' '+w+' ' in line:
                    flag = 1
                    break
            if flag:
                counter += 1
                print(counter)
                print(line)
                out.write(line)
            if counter >= 5000:
                counter = 0
                out.close()
                name += 1
                print(_get(name))
                out = open('/home/mo/word2vec_test/'+_get(name)+'.txt','w')
