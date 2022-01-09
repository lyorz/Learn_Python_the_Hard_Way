def new(num_buckets=256):
    """通过给定参数buckets初始化Map"""
    aMap=[]
    for i in range(0,num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap,key):
    """给定键，返回aMap存储的一个索引数字"""
    return hash(key)%len(aMap)

def get_bucket(aMap,key):
    """给定键，找到对应存储"""
    bucket_id=hash_key(aMap,key)
    return aMap[bucket_id]

def get_slot(aMap,key,default=None):
    """返回索引，键，"""