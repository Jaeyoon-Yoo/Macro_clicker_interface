
def run_storage(order, storages):
    if len(storages) == 0:
        print('<< empty storages !! >>')
    else:
        if order[0] == 'item':
            print(f"total items: {len(storages)}")
            for n, i in enumerate(storages.keys()):
                print(n, i)
        elif order[0] == 'length':
            if len(order) <= 1:
                for i in storages.keys():
                    print(f"{i} : {len(storages[i])}")
            else:
                for i in order[1:]:
                    if i in storages.keys():
                        print(f"{i} : {len(storages[i])}")
                    else:
                        print(f"<< {i} is not in storages >>")
        elif order[0] == 'all':
            if len(order) <= 1:
                for n, (i, j) in enumerate(storages.items()):
                    print(f"No.{n}\t: {i}\t|\t{type(j)}\t|\t{j}")
            else:
                for i in order[1:]:
                    if i in storages.keys():
                        print(f"<< info about {i}...>>")
                        print(f"{storages[i]}")
                    else:
                        print(f"<< {i} is not in storages >>")