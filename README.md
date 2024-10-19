# Catfact Generator
Make the module usable by running `BUILD.sh` ("You will have to do this manually if you are on Windows without WSL")

Requirements:
```bash
# python 3.8+
pip install requests
```

Example usage:
```python
>>> import catfact
>>> print(catfact.get_catfact())
'A Catfact'
```