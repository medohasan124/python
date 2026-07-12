
def write_item(item):
    path_file = "product.txt"

    with open(path_file,'a') as file:
        file.write(f"items is - {item} \n")

write_item("milk")
write_item("water")
write_item("chips")


def read_file(my_path):
   with  open(my_path,"r") as file:
        return file.read()

print(read_file("product.txt"))