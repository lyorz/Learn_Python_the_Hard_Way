def new(num_buckets=256):
    """通过给定参数buckets初始化Map"""
    aMap=[]
    for i in range(0,num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap,key):
    """关键字转整数"""
    return hash(key)%len(aMap)

def get_bucket(aMap,key):
    """使用hash_key来找到一个key所在的“bucket”"""
    bucket_id=hash_key(aMap,key)
    return aMap[bucket_id]

def get_slot(aMap,key,default=None):
    """使用get_bucket来获得一个key所在的“bucket”"""
    bucket=get_bucket(aMap,key)
    for i,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            return i,k,v
    return -1,key,default

def get(aMap,key,default=None):
    """"""
    i,k,v=get_slot(aMap,key,default=default)
    return v

def set(aMap,key,value):
    """若key存在，替换原有的值，否则创建新值"""
    bucket=get_bucket(aMap,key)
    i,k,v=get_slot(aMap,key)

    if i>=0:
        bucket[i]=(key,value)
    else:
        bucket.append((key,value))
    
def delete(aMap,key):
    """删除"""
    bucket=get_bucket(aMap,key)

    for i in range((len(bucket))):
        k,v=bucket[i]
        if key==k:
            del bucket[i]
            break

def list(aMap):
    """打印"""
    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print(k,v)

def dump(aMap):
    """备份所有内容"""
    bMap=new(len(aMap))
    for bucket in aMap:
        for k,v in bucket:
            set(bMap,k,v)
    return bMap