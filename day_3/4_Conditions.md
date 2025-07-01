if :
elif :
else

--

| Operator | Meaning |
| --- | --- |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=`  | Less than or equal to |
| `==`  | Equal to |
| `!=`  | Not equal to |

<!-- one line condition -->

fruit = 'Apple'
isApple = True if fruit == 'Apple' else False

<!-- vs -->

fruit = 'Apple'
isApple = False
if fruit == 'Apple' : isApple = True