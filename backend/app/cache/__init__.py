"""Cache module initialization"""

from app.cache.redis_client import RedisClient, get_redis_client
from app.cache.cache_decorator import cache_result

__all__ = ["RedisClient", "get_redis_client", "cache_result"]
