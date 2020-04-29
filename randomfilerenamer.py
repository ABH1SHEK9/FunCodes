#!/usr/bin/python3



import os,sys,random,string,glob

def main():
        
    img_dir = os.getcwd()
    print (img_dir)
    data_path = os.path.join(img_dir,'*jpg')
    
    files = glob.glob(data_path)
    print (files)
    j = 0
    used = []
    for i in files:
        j=j+4
        random.seed(j)
        #r = random.randrange(12, 9999, 1)
        r = randomStrings()
        print (i,r)
        used.append(i)
        os.rename(i, img_dir + "/" + str(r) + ".jpg")

    print("Finished!")


def randomStrings(sLength=9):
    alphbt = string.ascii_lowercase
    return ''.join(random.choice(alphbt for i in range(sLength)))

if __name__ == "__main__":
    main()


        
                


