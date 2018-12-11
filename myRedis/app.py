import redis

pool = redis.ConnectionPool(host='cs-prod-redis.vabidq.ng.0001.usw1.cache.amazonaws.com', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


pipe = r.pipeline()
pipe.hmset('aabb-cccdd-1112233', {
  'status': 'online',
  'properties': '{"defaultRoute": "wlan"}'
})
pipe.hmset('1278-14faa-123141a', {
  'status': 'online',
  'properties': '{"defaultRoute": "eth0"}'
})
pipe.execute()

print(r.hgetall("aabb-cccdd-1112233"))
print(r.hget("1278-14faa-123141a", 'properties'))