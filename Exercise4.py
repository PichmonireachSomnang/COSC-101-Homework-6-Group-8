def chunking_by(list, size):
    results = []
    x = len(list)
    excess = x % size
    chunk = x // size
    while chunk > 0:
        results.append(list[0:(size)])
        del list[0:(size)]
        chunk -=1
        continue
    if excess != 0:
        results.append(list[0:(excess)])
    return results
# list1 = [0,1,2,3,2,4,5]
# try:
#     Size = int(input("input your desired chunk size: "))
# except ValueError:
#     print("invalid input")
# print(chunking_by(list1, Size))