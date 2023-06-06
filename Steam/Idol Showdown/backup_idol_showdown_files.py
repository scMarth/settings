import shutil, os, sys

import user_file

workspace = os.getcwd()

# https://store.steampowered.com/account/remotestorage

src = r'C:\Users\{}\AppData\LocalLow\BestoGameStudios\Idol Showdown'.format(user_file.user_name)  # Replace with the source directory path
print(src)
sys.exit()
dst = workspace + r'\Idol Showdown'  # Replace with the destination directory path

dst_num = -1

for folder in os.listdir(workspace):
    folder_path = os.path.join(workspace, folder)

    if not os.path.isdir(folder_path):
        continue
    else:
        if r'Idol Showdown\Idol Showdown' not in folder_path:
            continue

    print('folder_path: {}'.format(folder_path))
    number = folder_path.split(r'Idol Showdown\Idol Showdown')[1]
    if number:
        number = int(number)

    if not number:
        number = 0
    number += 1

    if number > dst_num:
        dst_num = number

dst += str(dst_num)

print('src: {}'.format(src))
print('dst: {}'.format(dst))

if os.path.exists(dst):
    shutil.rmtree(dst)

# Create the destination directory if it doesn't exist
if not os.path.exists(dst):
    os.makedirs(dst)

# Copy the contents of the source directory to the destination directory
for item in os.listdir(src):
    src_item = os.path.join(src, item)
    dst_item = os.path.join(dst, item)
    if os.path.isdir(src_item):
        shutil.copytree(src_item, dst_item)
    else:
        shutil.copy2(src_item, dst_item)

print("Copy complete!")
