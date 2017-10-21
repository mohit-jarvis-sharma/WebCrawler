import os
import shutil

def reset():
    temp = os.listdir()
    for i in temp:
        if os.path.isdir(i) and not i.startswith('.'):
            shutil.rmtree(i)
    print('Crawler reset done')

def new_proj(name, seed):
    queue = name + '/queue.txt'
    crawled = name + '/crawled.txt'
    terms = name + '/terms'
    if not os.path.exists(name):
        print('Creating Project .. ' + name)
        os.makedirs(name)
    if not os.path.isfile(queue):
        write_file(queue, seed)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isdir(terms):
        os.mkdir(terms)
    print('Project files created')

def write_file(path , data):
    f = open(path , 'w')
    f.write(data)
    f.close()

def delete_contents(path):
    with open(path , 'w') as f:
        pass

def append_to_file(path, data):
    with open(path , 'a') as f:
        f.write(data + '\n')

def file_to_set(name):
    results = set()
    with open(name , 'rt') as f:
        for line in f:
            results.add(line.replace('\n' , ''))
    return results

def set_to_file(links, name):
    delete_contents(name)
    for link in sorted(links):
        append_to_file(name, link)

