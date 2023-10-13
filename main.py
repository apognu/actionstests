import redis

# 2

def main():
  cache = redis.StrictRedis(host="1.2.3.4", port=6379)
  value = cache.get("test")

  print(value)
