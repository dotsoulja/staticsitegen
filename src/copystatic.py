import os
import shutil


# copy contents from one directory to another recursively
def copy_static_recursive(source_dir, new_dir): 
    # if new directory exists, delete it recursively
    if os.path.exists(new_dir):
        print(f"deleting {new_dir} directory")
        shutil.rmtree(new_dir)
        print(f"deleted {new_dir} directory")
    # create the new directory
   
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    for filename in os.listdir(source_dir):
        from_path = os.path.join(source_dir, filename)
        new_path = os.path.join(new_dir, filename)
        print(f"copying from {from_path} to {new_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, new_path)
        else:
            copy_static_recursive(from_path, new_path)
