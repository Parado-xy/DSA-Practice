# Description
# TinyURL is a URL shortening service where you enter a URL 
# such as https://lintcode.com/problems/design-tinyurl and it returns a short URL 
# such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. T
# here is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

import random

class Solution:
    def __init__(self):
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._map = dict()
        self.key = self.get_rand()

    def get_rand(self):
        # Generate a random key.
        return ''.join(self.alphabet[random.randint(0, 61)] for _ in range(6))

    def encode(self, longUrl):
        # If the current key already exists in the map, generate a new random key. 
        while self.key in self._map: self.key = self.get_rand()
        # map the current random key to the longUrl
        self._map[self.key] = longUrl
        # Return the tinyurl 
        return f"https://tinyurl.com/{self.key}"

    def decode(self, shortUrl):
        # Split on forward slashes & take the last bit as the key 
        key = shortUrl.split('/')[-1]
        # Map and return it. 
        return self._map[key]