# Le binaire
quartet = 4 chiffres = 4 bits

| Bit 3 | Bit 2 | Bit 1 | Bit 0 |
|-------|-------|-------|-------|
|   0   |   0   |   0   |   0   |
|   0   |   0   |   0   |   1   |
|   0   |   0   |   1   |   0   |
|   0   |   0   |   1   |   1   |
|   0   |   1   |   0   |   0   |
|   0   |   1   |   0   |   1   |
|   0   |   1   |   1   |   0   |
|   0   |   1   |   1   |   1   |
|   1   |   0   |   0   |   0   |
|   1   |   0   |   0   |   1   |
|   1   |   0   |   1   |   0   |
|   1   |   0   |   1   |   1   |
|   1   |   1   |   0   |   0   |
|   1   |   1   |   0   |   1   |
|   1   |   1   |   1   |   0   |
|   1   |   1   |   1   |   1   |

Octet = 8 chiffres = 8 bits

| Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
|-------|-------|-------|-------|-------|-------|-------|-------|
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |   0   |

_Exemple:_
238 en octet =  *1 1 1 0 1 1 1 0*
_1_=**128** _1_=**64** _1_=**32** _0_=**16** _1_=**8** _1_=**4** _1_=**2** _0_=**1**

37843
**32768 16384 8192 4096 2048 1024 512 256 128 64 32 16 8 4 2 1**
_1001 0011 1101 0011_   
(**93D3**)

--- 
# Hexadecimal
Permet de simplifier la lecture du binaire (s'arrete à F)

| Binaire (4 bits) | Hexadécimal |
|------------------|-------------|
|       0000       |      0      |
|       0001       |      1      |
|       0010       |      2      |
|       0011       |      3      |
|       0100       |      4      |
|       0101       |      5      |
|       0110       |      6      |
|       0111       |      7      |
|       1000       |      8      |
|       1001       |      9      |
|       1010       |      A      |
|       1011       |      B      |
|       1100       |      C      |
|       1101       |      D      |
|       1110       |      E      |
|       1111       |      F      |

_exemple:_
_1010 1100 1011 0101 1111 0011_ = **ACB5F3**

En dev on utilise l'hexadecimal pour les couleur en _RGB_
**AC** = le rouge
**B5** = le vert
**F3** = le bleu
Converti en décimal cela donne: _AC_ =172 _B5_=181 _F3_= 243 
```css
body {
background-color: #ACB5F3;
color: 172 181 243;
}
```

La conversion d'un nombre binaire en un nombre hexadécimal est relativement simple. Les nombres binaires sont regroupés en groupes de quatre chiffres binaires, et chaque groupe est ensuite converti en son équivalent hexadécimal. Voici un exemple de conversion d'un nombre binaire en hexadécimal :

Prenons le nombre binaire `110110101011` et convertissons-le en hexadécimal :

1. Regroupez les chiffres binaires en groupes de quatre, en commençant par la droite. Si le nombre de chiffres binaires n'est pas un multiple de quatre, ajoutez des zéros à gauche pour compléter le dernier groupe. Dans ce cas, le groupe complet est `1101` et le groupe partiel est `0101`.

2. Convertissez chaque groupe en son équivalent hexadécimal. Voici la conversion :

   - `1101` en hexadécimal est équivalent à `D`.
   - `0101` en hexadécimal est équivalent à `5`.

3. Placez les chiffres hexadécimaux obtenus les uns à côté des autres pour obtenir la représentation hexadécimale du nombre binaire original. Dans notre exemple, `110110101011` en binaire est équivalent à `D5` en hexadécimal.

Donc, `110110101011` en binaire est équivalent à `D5` en hexadécimal.

--- 
# Décalage et rotation
Le décalage et la rotation de bits sont des opérations courantes dans la programmation informatique, généralement utilisées pour manipuler des valeurs binaires ou pour effectuer des opérations de manipulation de bits plus avancées. Voici ce que sont le décalage et la rotation de bits :

**1. Décalage de bits (Bit Shifting)** :
Le décalage de bits consiste à déplacer les bits d'une valeur binaire vers la gauche ou la droite. Il existe deux types principaux de décalage de bits :

- **Décalage à gauche (Left Shift)** : Lorsque vous effectuez un décalage à gauche, vous déplacez les bits vers la gauche en insérant des zéros à droite. Par exemple, si vous effectuez un décalage à gauche de 2 positions sur le nombre binaire `1101`, vous obtenez `110100` (les deux zéros à droite ont été ajoutés).

- **Décalage à droite (Right Shift)** : Lorsque vous effectuez un décalage à droite, vous déplacez les bits vers la droite. Le comportement peut varier selon le langage de programmation. Dans certains langages, un décalage à droite insère des zéros à gauche (décalage logique), tandis que dans d'autres langages, il conserve le bit de signe (décalage arithmétique).

Le décalage de bits est couramment utilisé pour la multiplication ou la division par des puissances de 2, ainsi que pour des opérations de masquage et de récupération de valeurs spécifiques à partir de données binaires.

**2. Rotation de bits (Bit Rotation)** :
La rotation de bits est similaire au décalage de bits, mais elle déplace les bits d'une manière circulaire, de sorte que les bits qui sortent d'un côté réapparaissent de l'autre côté. Il existe deux types principaux de rotation de bits :

- **Rotation à gauche (Left Rotate)** : Les bits sont déplacés vers la gauche, et ceux qui sortent à gauche réapparaissent à droite. Par exemple, si vous effectuez une rotation à gauche de 2 positions sur le nombre binaire `110110`, vous obtenez `011011` (les deux bits qui sont sortis à gauche sont réapparus à droite).

- **Rotation à droite (Right Rotate)** : Les bits sont déplacés vers la droite, et ceux qui sortent à droite réapparaissent à gauche.

La rotation de bits est utilisée dans des contextes où la position des bits est importante, comme la cryptographie, la compression de données et d'autres opérations où vous souhaitez conserver la structure des données binaires tout en les déplaçant.

Les décalages et les rotations de bits sont des opérations puissantes et utiles pour effectuer diverses manipulations sur les données binaires, mais il est important de comprendre comment elles fonctionnent dans le langage de programmation que vous utilisez, car le comportement peut varier d'un langage à l'autre.

_Voici quelques exemples de décalage et de rotation de bits en utilisant le langage de programmation Python. Python offre des opérateurs de décalage de bits (`<<` pour le décalage à gauche et `>>` pour le décalage à droite) et des opérateurs de rotation de bits (`rol` pour la rotation à gauche et `ror` pour la rotation à droite) via la bibliothèque `bitstring`._

**Exemple de décalage de bits :**

```python
# Décalage à gauche (Left Shift)
x = 5  # En binaire : 0101
result = x << 2  # Décalage à gauche de 2 positions
print(bin(result))  # Résultat en binaire : 10100 (équivalent à 20 en décimal)

# Décalage à droite (Right Shift)
y = 16  # En binaire : 10000
result = y >> 3  # Décalage à droite de 3 positions
print(bin(result))  # Résultat en binaire : 10 (équivalent à 2 en décimal)
```

**Exemple de rotation de bits :**

Pour effectuer des rotations de bits en Python, vous pouvez utiliser la bibliothèque `bitstring` :

```python
from bitstring import BitArray

# Rotation à gauche (Left Rotate)
x = BitArray(bin='110110')  # En binaire : 110110
result = x.rol(2)  # Rotation à gauche de 2 positions
print(result.bin)  # Résultat en binaire : 011011

# Rotation à droite (Right Rotate)
y = BitArray(bin='110110')  # En binaire : 110110
result = y.ror(2)  # Rotation à droite de 2 positions
print(result.bin)  # Résultat en binaire : 101101
```

Ces exemples illustrent comment effectuer des décalages et des rotations de bits en utilisant Python. Les opérations de décalage et de rotation de bits sont utiles dans de nombreux contextes de programmation, notamment pour la manipulation de données binaires, le codage et le décodage, ainsi que dans certains algorithmes de chiffrement et de traitement de données.
