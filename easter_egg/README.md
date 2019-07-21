# easter egg
Description:
```
There's a flag hidden on this website, can you find it?

(No brute force required. The flag is not on any teams page, you don't need to check any page that starts with "https://fbctf.com/teams/")
```

After searching `fb{` on all pages, found nothing

But searching for `{` found something interesting on `careers` page:
```html
<p>Facebook's Application Security team<span style="color:white">{</span>is seeking a passionate hacker to help us secure over 2 billion users....
```
And searching for `}`:
```html
<p>The Oculus Security Engineering team designs, builds, and supports the infrastructure and services<span style="color:white">}</span>that allow Oculus to move fast,...
```
Also found `<span style="color:white">f`, `<span style="color:white">b` etc...

I wrote [quick python script](solve.py) to combine all characters together:
```python
import re
text = open("careers",'r').read()
text = re.findall('''<span style="color:white">(.)</span>''',text)
print ''.join(text)
```

## Flag
> fb{we're_hiring}