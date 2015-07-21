import hashlib

def digest(method, hash):
  h = hashlib.new(method, hash.decode("hex"))
  return h.hexdigest()

ripemd160 = lambda x: digest("ripemd160", x)
sha256 = lambda x: digest("sha256", x)

__b58chars = "123456789" + \
  "ABCDEFGHJKLMNPQRSTUVWXYZ" + \
  "abcdefghijkmnopqrstuvwxyz"
__b58base = len(__b58chars)
 
def b58(hash):
  data = hash.decode("hex")
  long_value = 0
  for (i, c) in enumerate(data[::-1]):
    long_value += (256**i) * ord(c)
  result = ""
  while long_value >= __b58base:
    div, mod = divmod(long_value, __b58base)
    result = __b58chars[mod] + result
    long_value = div
  result = __b58chars[long_value] + result
  nPad = 0
  for x in data:
    if x != '\0': break
    nPad += 1
  return (__b58chars[0]*nPad) + result

footprint = raw_input()
footprint = "00" + ripemd160(footprint)
footprint = footprint + sha256(sha256(footprint))[:8]
print b58(footprint)
