import json
import numpy as np
import wget
import redis
import sys
import time


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap

#url = "https://raw.githubusercontent.com/json-iterator/test-data/master/large-file.json"
#filename = wget.download(url)
filename = "./large-file.json"

with open(filename, 'r', encoding='utf8') as json_file:
    large_json = json.load(json_file)
    large_string = json.dumps(large_json)
    large_list = large_string.split(' ')
    large_set = set(large_list)
    nums = np.linspace(0, len(large_list) - 1, num=len(large_list) - 1)
    large_zset = {large_list[int(n)]: int(n) for n in nums}


rdb = redis.Redis(host='localhost', port=6379)

'''
rdb.set('str', large_string)

for elem in large_list:
    rdb.rpush('list', elem)
'''
rdb.sadd('hset', *large_set)
rdb.zadd('zset', large_zset)


start = time.time()
rdb.lrange('list', 0, 5000)
end = time.time()
print("lrange 0-5000: {:.02f}ms".format(end - start))

start = time.time()
rdb.append('string', "SOme sTRange strinG!")
end = time.time()
print("String append {:.02f}ms".format(end - start))

start = time.time()
rdb.sismember('set', '42424242')
end = time.time()
print("Set sismember {:.02f}ms".format(end - start))

start = time.time()
rdb.sadd('set', '424242424')
end = time.time()
print("Set sadd {:.02f}ms".format(end - start))

start = time.time()
rdb.lpush('list', *large_list[:6000])
end = time.time()
print("List push 6000 {:.02f}ms".format(end - start))


start = time.time()
rdb.zrange('zset', 0, 6000)
end = time.time()
print("Zrange 6000 {:.02f}ms".format(end - start))

start = time.time()
#rdb.delete('str', 'list', 'hset', 'zset')
end = time.time()
print("delete {:.02f}ms".format(end - start))

