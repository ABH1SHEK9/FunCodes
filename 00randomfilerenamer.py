#!/usr/bin/python3
# year2019
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

        j+= 4
        #random.seed(j)
        r = random.randrange(8, 13, 1)
        r = randomStrings()
        print (i,r)
        if (r in used):
                print ("exists")
                continue
        else:
                r = randomStrings(14)
                used.append(r)
                os.rename(i, img_dir + "/" + str(r) + ".jpg")

        
         

    print("Finished!")
    print (used)


def randomStrings(sLength=9):
    alphbt = string.ascii_letters
    return ''.join(random.choice(alphbt) for i in range(sLength))

if __name__ == "__main__":
    main()


        
                


