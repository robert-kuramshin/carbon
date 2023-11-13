import urllib3

# async http client connection pool
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE')


def httpRequest(url, values=None, headers=None, method='POST', timeout=5):
  try:
    result = http.request(
      method,
      url,
      fields=values,
      headers=headers,
      timeout=timeout)
  except BaseException as err:
    raise Exception("Error requesting %s: %s" % (url, err))

  if result.status != 200:
    raise Exception("Error response %d from %s" % (result.status, url))

  return result.data
