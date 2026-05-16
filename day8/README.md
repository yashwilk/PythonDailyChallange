`@dataclass` - instead of scattering magic numbers and settings throughout your code, everything lives in one place.

## Syntax

```python
from dataclasses import dataclass

@dataclass
class Config:
    host: str = "localhost"
    port: int = 5432
    debug: bool = False
```

## Calling the Values

```python
config = Config()

print(config.host)   # 

## Overriding Values

```python
config = Config(host="12.12.12", debug=True)
print(config)  # Config(host='12.12.12', port=5432, debug=True)
```

---

## GRU Config Fields

### `use_aux_targets: bool = True`

Auxiliary targets help the model learn better by training on additional related information.

If predicting house price:
- **Main target:** price
- **Auxiliary targets:** number_of_rooms, area, location_score

```python
if config.use_aux_targets:
    loss = main_loss + aux_loss
else:
    loss = main_loss
```

### `use_online_learning: bool = True`

Should the model learn continuously from new incoming data? New data arrives -> update model.

```python
if config.use_online_learning:
    model.partial_fit(new_data)
```
