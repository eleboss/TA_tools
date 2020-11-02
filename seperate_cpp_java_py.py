import os
from zipfile import ZipFile
from distutils.dir_util import copy_tree


process_dir = "/home/eleboss/Documents/"
rootdir = process_dir + "COMP3270_1A_2020-as1"
cpp_path = process_dir + "COMP3270_1A_2020-as1_cpp"
py_path = process_dir + "COMP3270_1A_2020-as1_py"
java_path = process_dir + "COMP3270_1A_2020-as1_java"
# os.mkdir(cpp_path)
# os.mkdir(py_path)
# os.mkdir(java_path)
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        # print (subdir + os.sep)
        if filepath.endswith(".cpp"):
            try:
                os.mkdir(cpp_path + os.sep + subdir.split(os.sep)[5])
            except OSError:
                print("skip")
            print(subdir)
            copy_tree(subdir, cpp_path + os.sep + subdir.split(os.sep)[5])
            print (cpp_path + os.sep + subdir.split(os.sep)[5])
            break
        if filepath.endswith(".py"):
            try:
                os.mkdir(py_path + os.sep + subdir.split(os.sep)[5])
            except OSError:
                print("skip")
            print(subdir)
            copy_tree(subdir, py_path + os.sep + subdir.split(os.sep)[5])
            print (py_path + os.sep + subdir.split(os.sep)[5])
            break
        if filepath.endswith(".java"):
            try:
                os.mkdir(java_path + os.sep + subdir.split(os.sep)[5])
            except OSError:
                print("skip")
            print(subdir)
            copy_tree(subdir, java_path + os.sep + subdir.split(os.sep)[5])
            print (java_path + os.sep + subdir.split(os.sep)[5])
            break
