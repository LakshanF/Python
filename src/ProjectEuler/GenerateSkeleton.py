# This will create a template python program

outDir='./src/ProjectEuler/1_100/'

for suffix in range(18, 21):
    fileName = outDir + str(suffix) + '.py'
    f = open(fileName, 'w')
    for i in range(5):
        f.write('# \n')
    f.write('\n')
    f.write('import time\n')
    f.write('start_time = time.time()\n')
    for i in range(10):
        f.write('\n')
    f.write('print(\'--- %s seconds ---\' % (time.time() - start_time))\n')
    f.close()