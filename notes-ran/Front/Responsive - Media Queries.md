```html
<!DOCTYPE html>
<html lang="en"
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
<link href="style.css" rel="stylesheet">
</head>
<body>
<h1>blablablablabal</h1>
</body>
</html>
```

```css
h1 {
  color: blue;
}

@media (max-width: 800px) {
  h1 {
    color: red;
  }
}
```

**Média Queries**
On utilise la balise **@media** avec une taille _(max-width:800px)_
Les propriétés s'appliquerons quand l'écran passe en dessous de 800px

_exemple taille écran_:

xs **<** 576px
sm **>=** 576px
md **>=** 768px
lg **>=** 992px
xl **>=** 1200px
xxl **>=** 1400px
