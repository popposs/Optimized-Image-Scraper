from config import options
import redis


_host = options['host']
_port = options['port']
_db = options['db']

cache_client = redis.StrictRedis(host=_host, port=_port, db=_db, charset="utf-8", decode_responses=True)

