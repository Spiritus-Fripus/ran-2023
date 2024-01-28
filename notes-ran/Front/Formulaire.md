```html
<form method="post" action="page.php">
    <label for="firstname">Prénom</label>
    <input type="text" id="firstname">
    <label for="mail">Mail</label>
    <input type="mail" id="mail" placeholder="Your mail">
    <input value="ok" type="submit">
</form>
```
# Label
```html
<label for="radio_gaga">
<input type="radio" id="radio_gaga">
```
**for** doit correspondre à **id**
# Input
```html
<input type="mail">
<input type="date">
<input type="datetime">
<input type="number">
<input type="color">
```

```html
<textarea></textarea>
```
_"**Textearea"** et une balise de type input mais en pair !_
```html
<input type="checkbox">
<input type="checkbox">
```
Utile pour les QCM , ne pas confondre avec les boutons radio **(plusieurs choix possible)**
```html
<input type="radio">
<input type="radio">
<input type="radio">
```
Les boutons radio ne propose que **1 choix possible** (Coche/décoche)

# Name
```html
<input type="radio" name="liste1">
<input type="radio" name="liste1">
<input type="radio" name="liste1">

<input type="radio" name="liste2">
<input type="radio" name="liste2">
<input type="radio" name="liste2">
```
Permet de différencier des listes d'input

# Required

```html
<label for="lastname">Nom*</label>
<input type="text" id="lastname" required>
```
**Required** indique un champ obligatoire 

# Select
```html
<select>
	<option value="">Selectionez</option>
	<option value="1">.....</option>
	<option value="2">.....</option>
	<option value="3">.....</option>
</select>
```
