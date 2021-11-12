name="Snehal Pawar"
print(name)
import math
import requests

print('  π: {:.30f}'.format(math.pi))
print('  e: {:.30f}'.format(math.e))
print('nan: {:.30f}'.format(math.nan))
print('inf: {:.30f}'.format(math.inf))

url="http://127.0.0.1:9000/api/project-master-controller/get-projects"
value=requests.get(url)
print(value.text)
