import os

train_path = "E:\\Github\\MUNIT-master\\datasets\\real2paint\\test_B"

with open("test_b.txt", 'w') as file:

    with os.scandir(train_path) as it:
        for entry in it:
            if entry.name.endswith(".jpg") and entry.is_file():
                print(entry.name, entry.path)
                file.write("./"+entry.name+'\n')