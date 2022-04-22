
'''
# to call single module

import file10_modu_pack

file10_modu_pack.func()

''
# to call multiple package from different files

from package import 1st_filename, 2nd_filename

1st_filename.func2()
 2nd_filename.dunc1()
 ''

''
# to import sub package from file

from package.sub_package_foldername import sub_filename
sub_package_filename.func()
''

# to make a simple file  folder package file give name " __init_py " then only from that file module can be inported

'''