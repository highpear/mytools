import glob, sys, os

def main():
    argv = sys.argv

    if(len(argv) != 3):
        print('usage:')
        print('python ren.py [directory_name] [string]')
        sys.exit()

    dirname = argv[1]    # path to directory
    addedstr = argv[2]   # this string is added to head of all file names

    files = glob.glob(dirname + '/*.flac')

    if(len(files) == 0):
        print('no flac file in this directory')
        sys.exit()

    # preview
    for file in files:
        bname = os.path.basename(file)
        newname = addedstr + bname
        print(bname, '->', newname)

    print('execute renaming ? (yes or no)')
    ans = input()
    if(ans == 'yes' or ans == 'y'):
        for file in files:
            bname = os.path.basename(file)
            newname = addedstr + bname
            newname = os.path.join(dirname, newname)
            os.rename(file, newname)
            print(file, 'was renamed to', newname)
        print('finished')
    else:
        sys.exit()


if __name__ == '__main__':
    main()