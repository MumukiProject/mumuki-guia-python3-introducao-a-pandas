¡Perfecto! :clap: Probablemente hiciste algo como:

```python
ム len(cines["city_name"].unique())
254
```

Como esta operación es tan común, contamos con un atajo, la operación `nunique`:

```python
ム cines["city_name"].nunique()
254
```
