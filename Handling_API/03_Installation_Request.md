# ✅ How to Install requests :
## Open terminal / command prompt and run:
```
pip install requests
```
## For Python 3 (if needed):
```
pip3 install requests
```
## ✅ How to Check if It's Installed
```
pip show requests
```

## ✅ Once installed, you can use it like this:
```
import requests

res = requests.get("https://api.github.com")
print(res.status_code)
print(res.json())

```