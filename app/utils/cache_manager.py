from cachetools import Cache, LRUCache

# Create an instance of the cache with a maximum size of 100
cache: Cache = LRUCache(maxsize=100)

def clear_cached_data(cached_data):
    """
    Clear any cached data or resources associated with the user session.
    """
    # Remove the cached data from the cache
    cache.pop(cached_data, None)
