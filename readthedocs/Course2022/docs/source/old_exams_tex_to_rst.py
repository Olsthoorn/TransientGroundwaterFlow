#! Python3

# Gegenerating documentation from the old Exam bundels 
# TO 2022-5-27

# Convert the bundels to rst Files using pandoc

import os
from collections import Counter


def get_nextLine(fin, counter):
    while True:
        s = fin.readline()
        if not s:
            print('Done, {} lines read, {} figures found'.
                  format(counter['lines'], counter['figures']))
        yield s
        counter.update(['lines'])

syllabus = '/Users/Theo/Instituten-Groepen-Overleggen/IHE/git_TransientGroundwaterFlow/SyllabusUptoDate/'
home     = '/Users/Theo/Instituten-Groepen-Overleggen/IHE/git_TransientGroundwaterFlow/readthedocs/Course2022/'
docs     = os.path.join(home, 'docs/')
source   = os.path.join(docs, 'source/')
build    = os.path.join(docs, 'build/') # not needed here

for d in [syllabus, home, docs, source]:
    assert os.path.isdir(d), FileExistsError(d)

os.chdir(source)
os.getcwd()

basename_1 = 'exams_from_2006'
basename_2 = 'exams_from_2006' + '+answers'
texfile_1  = os.path.join(syllabus, basename_1 + '.tex')
texfile_2  = os.path.join(syllabus, basename_2 + '.tex')
tmpfile_1  = os.path.join(source,   basename_1 + '.tmp')
tmpfile_2  = os.path.join(source,   basename_2 + '.tmp')
rstfile_1  = os.path.join(source,   basename_1 + '.rst')
rstfile_2  = os.path.join(source,   basename_2 + '.rst')

for fname in [texfile_1, texfile_2]:
    assert os.path.isfile(fname), FileNotFoundError(fname)

# pandoc command setup for converting tex to rst
options = ' '.join([
    '-s',
    '-f latex',
    '-t rst',
    '--verbose',
    '--wrap=none',
    '--default-image-extension=png',
    '-o',
    ])

# pandoc commands
pandoc_cmd_1 = ' '.join(['pandoc', options, tmpfile_1, texfile_1])
pandoc_cmd_2 = ' '.join(['pandoc', options, tmpfile_2, texfile_2])

# executed them
os.system(pandoc_cmd_1)
os.system(pandoc_cmd_2)

counter = Counter()

# Add title of file as TOC top entry
with open(tmpfile_1, 'r') as fin:
    with open(rstfile_1, 'w') as fout:
        # Put title on top of .rst file
        fout.write('==============\n')
        fout.write('Previous exams\n')
        fout.write('==============\n')
        fout.write('\n')
        
        line = get_nextLine(fin, counter)
        
        while True:
            s = next(line)
            if not s:
                break
            
            fout.write(s) 

           
# Add title of file as TOC top entry 
with open(tmpfile_2, 'r') as fin:
    with open(rstfile_2, 'w') as fout:
        # Put title on top of .rst file.
        fout.write('===========================\n')
        fout.write('Previous exams with answers\n')
        fout.write('===========================\n')
        fout.write('\n')
        
        line = get_nextLine(fin, counter)
        
        while True:
            s = next(line)
            if not s:
                break
            
            fout.write(s) 
            
os.system(' '.join(['rm', tmpfile_1, tmpfile_2]))
print('Done.')    
    
