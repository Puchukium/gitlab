horiz = '\u2500'
vert = '\u2502'
ul = '\u250c'
ur = '\u2510'
ll = '\u2514'
lr = '\u2518'


# Acá debe colocar su nombre! Luego ejecute el programa para ver el resultado
name = "Ian Mendez"


width = len(name) + 4
top = ul + horiz*(width-2) + ur
middle = vert + ' ' + name + ' ' + vert
bottom = ll + horiz * (width-2) + lr
lines = [top] + [middle] + [bottom]
result = '\n'.join(lines)

print(result)