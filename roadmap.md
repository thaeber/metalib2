## Proposed features
- [ ] Typed accessors

### Typed accessors

Enable type conversion or type save access to metadata properties inspired by the `environs` package.
```python
metadata._path('source')
metadata._path['source']
metadata._path.source

metadata._datetime['date']

metadata._quantity['flowrate']
```