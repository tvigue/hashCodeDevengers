import sys

nb_pictures = 0
pictures = []

with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        if i == 0:
            nb_pictures = int(line)
        else:
            orientation, _ , *tags = line.split()
            pictures.append({
                'orientation': orientation,
                'tags': tags,
                'idx': i-1,
            })

print(pictures)


def find_next(actual_picture, pictures):
    for tag in actual_picture['tags']:
        for i, picture in enumerate(pictures):
            if tag in picture['tags']:
                return i
    return -1

def find_next_vertical(actual_picture, pictures):
    for tag in actual_picture['tags']:
        for i, picture in enumerate(pictures):
            if picture['orientation'] == 'H':
                continue
            if tag in picture['tags']:
                return i
    return -1

actual_picture = pictures.pop(0)
res = [actual_picture]
res_nb = 1
if actual_picture['orientation'] == 'V':
    is_next_vertical = True
else:
    is_next_vertical = False
while pictures:
    print(len(pictures))
    if is_next_vertical:
        idx = find_next_vertical(actual_picture, pictures)
        if idx == -1:
            idx = 0
            while pictures[idx]['orientation'] == 'H':
                idx +=1
    else:
        res_nb += 1
        idx = find_next(actual_picture, pictures)
        if idx == -1:
            idx = 0
    res.append(pictures[idx])
    actual_picture = pictures[idx]
    pictures.pop(idx)
    if actual_picture['orientation'] == 'V':
        is_next_vertical = not is_next_vertical

print(res)

with open(sys.argv[1].replace('txt', 'out'), 'w') as f:
    f.write(str(res_nb))
    f.write('\n')
    next_vertical = True
    for picture in res:
        if picture['orientation'] == 'H':
            f.write(str(picture['idx']))
            f.write('\n')
        else:
            f.write(str(picture['idx']))
            if not next_vertical:
                f.write('\n')
            else:
                f.write(' ')
            next_vertical = not next_vertical

