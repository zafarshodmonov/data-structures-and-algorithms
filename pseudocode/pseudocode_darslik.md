# Pseudocode (Psevdokod) bo'yicha to'liq darslik

> **Maqsad:** algoritmni qog'ozda tahlil qilib, uni aniq, bir ma'noli pseudocode'ga aylantirish va undan **C, C++, Python** kodlarini deyarli mexanik tarzda hosil qilish.

---

## Mundarija

1. Pseudocode nima va nima uchun kerak
2. Ish jarayoni: qog'ozdan koddan gacha
3. Yagona uslub (convention) — o'zingizning "standart"ingiz
4. Ma'lumot turlari va o'zgaruvchilar
5. Operatorlar
6. Input / Output
7. Shartli operatorlar (if / else)
8. Sikllar (loops)
9. Funksiyalar va procedure'lar
10. Massivlar, 2D massivlar, stringlar
11. Struct / Record va murakkab ma'lumot tuzilmalari
12. Rekursiya
13. Invariant, precondition, postcondition
14. Complexity analysis pseudocode'dan
15. Pseudocode → C / C++ / Python tarjima jadvali
16. Klassik andozalar (templates)
17. To'liq misol: Binary Search (tahlildan 3 tilgacha)
18. To'liq misol: Dynamic Programming (Knapsack)
19. To'liq misol: BFS (graph)
20. Ko'p uchraydigan xatolar
21. Tekshiruv ro'yxati (checklist)
22. Mashqlar va yechimlar

---

## 1. Pseudocode nima va nima uchun kerak

**Pseudocode** — algoritmni biror dasturlash tilining sintaksisiga bog'lanmagan, lekin **aniq va bir ma'noli** tarzda yozish usuli.

| Tabiiy til (inson tili) | Pseudocode | Haqiqiy kod |
|---|---|---|
| Noaniq, ko'p ma'noli | Aniq, lekin sintaksissiz | Aniq va sintaksisli |
| "Massivdagi eng kattasini top" | `max ← A[0]; for i in 1..n-1: ...` | `int mx = a[0]; for (...)` |

### Nima uchun kerak?

1. **Fikrni til sintaksisidan ajratadi.** `;`, `{}`, `#include` haqida o'ylamasdan, faqat *mantiq* ustida ishlaysiz.
2. **Bir marta yozib, ko'p tilga o'giriladi.** Sizning holatingizda: 1 ta pseudocode → C, C++, Python.
3. **Xatoni erta topadi.** Mantiqiy xato pseudocode bosqichida topilsa, debug qilish 10 baravar arzon.
4. **Complexity'ni ko'rish oson.** Sikl ichida sikl bo'lsa, $O(n^2)$ ekani pseudocode'dayoq ko'rinadi.
5. **Muloqot vositasi.** Tanlovlarda, jamoada, intervyuda algoritmni tushuntirish uchun.

### Pseudocode nima **emas**

- Bu rasmiy til **emas** — yagona "to'g'ri" standart yo'q (CLRS, Knuth, Sedgewick har xil yozadi).
- Bu tabiiy til **emas** — "shunchaki eng kattasini topamiz" pseudocode emas, bu tavsif.
- Bu yashirin kod **emas** — `vector<int>::iterator it = ...` kabi til-xos tafsilotlarni yozmang.

**Oltin qoida:** *Pseudocode'ni boshqa dasturchi (yoki 3 oydan keyingi o'zingiz) o'qib, ikkilanmasdan istalgan tilga o'gira olishi kerak.*

---

## 2. Ish jarayoni: qog'ozdan kodgacha

Siz allaqachon shu yo'ldan borasiz. Uni aniq bosqichlarga ajratamiz:

```
1. Masalani tushunish       → input/output, cheklovlar (constraints)
2. Qo'lda misollar yechish  → kichik misol, edge case'lar
3. G'oya (idea) topish      → qaysi paradigma? (greedy, DP, BFS, binary search, ...)
4. Pseudocode yozish        → aniq, bir ma'noli
5. Pseudocode'ni qo'lda "yurgizish" (trace) → misolda tekshirish
6. Complexity hisoblash     → cheklovlarga sig'adimi?
7. 3 tilga o'girish         → C, C++, Python
8. Test                     → misollar + edge case'lar
```

### Muhim: 5-bosqich — **Trace (dry run)**

Pseudocode yozgach, uni **jadval** bilan qo'lda bajaring:

Masalan, `max` topish, `A = [3, 7, 2]`:

| qadam | i | A[i] | mx |
|---|---|---|---|
| boshlanish | — | — | 3 |
| 1 | 1 | 7 | 7 |
| 2 | 2 | 2 | 7 |

Natija: `7`. Trace qilmagan pseudocode — tekshirilmagan kod bilan barobar.

### Cheklovlardan algoritm tanlash (tez jadval)

| $n$ | Ruxsat etilgan complexity (~1 soniyada) |
|---|---|
| $n \le 10$ | $O(n!)$ |
| $n \le 20$ | $O(2^n \cdot n)$ |
| $n \le 500$ | $O(n^3)$ |
| $n \le 5000$ | $O(n^2)$ |
| $n \le 10^5 - 10^6$ | $O(n \log n)$ |
| $n \le 10^7 - 10^8$ | $O(n)$ |
| $n \le 10^{18}$ | $O(\log n)$ yoki $O(1)$ |

---

## 3. Yagona uslub (convention)

Pseudocode'da yagona qat'iy standart yo'q, shuning uchun **o'zingizniki**ni belgilab, doim unga rioya qiling. Quyida tavsiya etiladigan uslub (kitob bo'ylab shu uslubdan foydalanamiz).

### 3.1. Asosiy qoidalar

| Qoida | Tanlov |
|---|---|
| Indekslash | **0-based** (C, C++, Python bilan mos) |
| Oraliq | **Yarim ochiq** `[l, r)` — `l` kiradi, `r` kirmaydi (kerak bo'lsa, aniq yozing) |
| Qiymat berish | `x ← 5` (yoki `x = 5`; muhimi — yagona bo'lsin) |
| Tenglikni tekshirish | `x = 5` (yoki `x == 5`) |
| Blok chegarasi | **Indentatsiya (chekinish)** + `:` |
| Sikl chegaralari | `for i ← 0 to n-1` (ikkala chegara ham **kiradi**) |
| Izoh | `// izoh` |
| Qaytarish | `return x` |
| Mantiqiy | `and`, `or`, `not` |
| Bo'sh qiymat | `NIL` |
| Cheksizlik | `∞` yoki `INF` |

> **Eng muhim tanlov — indeks va oraliq konventsiyasi.** Off-by-one xatolarining 80% shu yerdan chiqadi. Pseudocode boshida bir marta e'lon qiling.

### 3.2. Pseudocode sarlavhasi (header)

Har bir algoritm oldidan quyidagini yozish odat bo'lsin:

```
ALGORITHM: MaxElement
INPUT:  A[0..n-1] — butun sonlar massivi, n ≥ 1
OUTPUT: A dagi eng katta element
TIME:   O(n)
SPACE:  O(1)
```

Bu 4 qator sizni **spetsifikatsiya**ni o'ylashga majbur qiladi.

### 3.3. Asosiy sintaksis — bir qarashda

```
// O'zgaruvchiga qiymat berish
x ← 10
x ← x + 1

// Shart
if x > 5:
    ...
else if x = 5:
    ...
else:
    ...

// Sikllar
for i ← 0 to n-1:
    ...

while shart:
    ...

repeat:
    ...
until shart

// Funksiya
function Sum(A, n):
    ...
    return s

// Massiv
A ← array of size n
A[i] ← 5
```

---

## 4. Ma'lumot turlari va o'zgaruvchilar

Pseudocode'da turlar **mantiqiy** darajada yoziladi. Til-xos tur (`long long`, `unsigned`) emas, **ma'no** muhim.

| Pseudocode | Ma'nosi | C | C++ | Python |
|---|---|---|---|---|
| `integer` | butun son | `int` / `long long` | `int` / `long long` | `int` |
| `real` | haqiqiy son | `double` | `double` | `float` |
| `boolean` | `true` / `false` | `bool` (`stdbool.h`) | `bool` | `bool` |
| `char` | bitta belgi | `char` | `char` | `str` (uzunligi 1) |
| `string` | matn | `char[]` | `std::string` | `str` |
| `array` | massiv | `int a[N]` | `vector<int>` | `list` |

### Turni qachon yozish kerak?

Har doim emas. Quyidagi holatlarda **yozing**:

1. Overflow xavfi bor bo'lsa: `sum: integer (64-bit)`
2. Butun bo'lish kerak bo'lsa: `mid ← ⌊(l + r) / 2⌋`
3. Haqiqiy son aniqligi muhim bo'lsa

> **Competitive programming maslahati:** cheklovlarni ko'ring. Agar javob $10^{9}$ dan katta bo'lishi mumkin bo'lsa, pseudocode'ga `// 64-bit kerak` deb izoh yozing. Kodga o'girganda `long long` ishlatasiz.

### Butun bo'lish va qoldiq

Bu joyda tillar farq qiladi, shuning uchun pseudocode'da **aniq** belgilang:

```
q ← ⌊a / b⌋      // butun bo'lish (floor)
r ← a mod b      // qoldiq
```

| Amal | C / C++ | Python |
|---|---|---|
| `⌊a / b⌋` (musbat) | `a / b` | `a // b` |
| `a mod b` (musbat) | `a % b` | `a % b` |
| `a / b` (real) | `(double)a / b` | `a / b` |

**Diqqat (manfiy sonlar):** C/C++ da `-7 / 2 = -3` (nolga qarab yaxlitlaydi), Python da `-7 // 2 = -4` (pastga yaxlitlaydi). Manfiy sonlar bo'lsa, pseudocode'da buni alohida izohlang.

---

## 5. Operatorlar

### 5.1. Arifmetik

| Pseudocode | Ma'nosi |
|---|---|
| `+`, `-`, `×` yoki `*` | qo'shish, ayirish, ko'paytirish |
| `/` | real bo'lish |
| `⌊a / b⌋` | butun bo'lish |
| `a mod b` | qoldiq |
| `a^b` | daraja |
| `⌈x⌉`, `⌊x⌋` | ceiling, floor |

### 5.2. Taqqoslash

`=`, `≠`, `<`, `>`, `≤`, `≥`

### 5.3. Mantiqiy

`and`, `or`, `not`

### 5.4. Bit operatsiyalari

| Pseudocode | Ma'nosi | C / C++ / Python |
|---|---|---|
| `a AND b` | bitli VA | `a & b` |
| `a OR b` | bitli YOKI | `a \| b` |
| `a XOR b` | bitli XOR | `a ^ b` |
| `a << k` | chapga siljitish | `a << k` |
| `a >> k` | o'ngga siljitish | `a >> k` |

> Bit operatsiyalarida `a & b` ni pseudocode'da `AND` deb yozish tavsiya etiladi — `&` va `&&` chalkashmasligi uchun.

### 5.5. Swap (almashtirish)

```
swap(a, b)
// yoki
a ↔ b
```

| Til | Kod |
|---|---|
| C | `int t = a; a = b; b = t;` |
| C++ | `swap(a, b);` |
| Python | `a, b = b, a` |

---

## 6. Input / Output

Pseudocode'da I/O'ni **minimal** yozing. Format tafsilotlari (`scanf`, `cin`) kerak emas.

```
read n
read A[0..n-1]

print result
print "YES" if ok else "NO"
```

Tarjima:

| Pseudocode | C | C++ | Python |
|---|---|---|---|
| `read n` | `scanf("%d", &n);` | `cin >> n;` | `n = int(input())` |
| `read A[0..n-1]` | `for (...) scanf("%d", &a[i]);` | `for (...) cin >> a[i];` | `a = list(map(int, input().split()))` |
| `print x` | `printf("%d\n", x);` | `cout << x << "\n";` | `print(x)` |

> **Competitive programming eslatmasi:** katta input'da C++ da `ios::sync_with_stdio(false); cin.tie(nullptr);`, Python da `sys.stdin.readline` ishlating. Bu — pseudocode'ga emas, **implementatsiyaga** tegishli.

---

## 7. Shartli operatorlar

### 7.1. Sintaksis

```
if shart:
    ...
```

```
if shart:
    ...
else:
    ...
```

```
if shart1:
    ...
else if shart2:
    ...
else:
    ...
```

### 7.2. Misol: sonning ishorasi

```
function Sign(x):
    if x > 0:
        return 1
    else if x < 0:
        return -1
    else:
        return 0
```

**C:**
```c
int sign(int x) {
    if (x > 0) return 1;
    else if (x < 0) return -1;
    else return 0;
}
```

**C++:**
```cpp
int sign(int x) {
    if (x > 0) return 1;
    if (x < 0) return -1;
    return 0;
}
```

**Python:**
```python
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
```

### 7.3. Murakkab shartlar

Shart murakkab bo'lsa, **nomlangan mantiqiy o'zgaruvchi**ga ajrating:

```
// Yomon:
if (a > 0 and b > 0 and (a + b) mod 2 = 0) or c = 0:
    ...

// Yaxshi:
bothPositive ← (a > 0 and b > 0)
evenSum ← ((a + b) mod 2 = 0)
if (bothPositive and evenSum) or c = 0:
    ...
```

### 7.4. Short-circuit

`A and B` da `A` yolg'on bo'lsa, `B` hisoblanmaydi. Bu — indeksdan chiqib ketishdan himoyalaydi:

```
if i < n and A[i] = x:    // to'g'ri: avval chegara
    ...
```

Uchala tilda (C, C++, Python) ham shunday ishlaydi. Tartibni **saqlang**.

---

## 8. Sikllar

### 8.1. `for` — sanaluvchi sikl

```
for i ← 0 to n-1:          // i = 0, 1, ..., n-1  (ikkala chegara kiradi)
    ...

for i ← n-1 down to 0:     // i = n-1, n-2, ..., 0
    ...

for i ← 0 to n-1 step 2:   // i = 0, 2, 4, ...
    ...
```

| Pseudocode | C / C++ | Python |
|---|---|---|
| `for i ← 0 to n-1` | `for (int i = 0; i < n; i++)` | `for i in range(n):` |
| `for i ← 1 to n` | `for (int i = 1; i <= n; i++)` | `for i in range(1, n + 1):` |
| `for i ← n-1 down to 0` | `for (int i = n-1; i >= 0; i--)` | `for i in range(n-1, -1, -1):` |
| `for i ← 0 to n-1 step 2` | `for (int i = 0; i < n; i += 2)` | `for i in range(0, n, 2):` |

> **Python `range` tuzog'i:** `range(a, b)` da `b` **kirmaydi**. Pseudocode `to` da esa kiradi. Shuning uchun `to n-1` → `range(n)`.

### 8.2. `for each` — elementlar bo'yicha

```
for each x in A:
    ...
```

- Python: `for x in A:`
- C++: `for (int x : A)`
- C: `for (int i = 0; i < n; i++) { int x = a[i]; ... }`

### 8.3. `while`

```
while shart:
    ...
```

Misol — Evklid algoritmi (GCD):

```
function GCD(a, b):
    while b ≠ 0:
        r ← a mod b
        a ← b
        b ← r
    return a
```

**C:**
```c
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}
```

**C++:**
```cpp
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}
```

**Python:**
```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

### 8.4. `repeat ... until` (do-while)

Kamida bir marta bajariladigan sikl:

```
repeat:
    ...
until shart
```

- C/C++: `do { ... } while (!shart);` — **diqqat: shart teskarisi!**
- Python: `while True: ...; if shart: break`

### 8.5. `break` va `continue`

```
for i ← 0 to n-1:
    if A[i] < 0:
        continue          // keyingi iteratsiyaga o'tish
    if A[i] = target:
        break             // sikldan chiqish
```

### 8.6. Sikl invarianti (muhim!)

Siklni yozishdan oldin o'zingizdan so'rang:

> **"Har bir iteratsiya boshida qaysi shart doim to'g'ri?"**

Bu shart — **loop invariant**. U siklning to'g'riligini isbotlaydi (13-bo'limga qarang).

---

## 9. Funksiyalar va procedure'lar

### 9.1. Sintaksis

```
function Nomi(param1, param2):
    ...
    return qiymat
```

Qiymat qaytarmasa — `procedure`:

```
procedure Nomi(param1, param2):
    ...
```

### 9.2. Parametr uzatish: qiymat yoki havola

Bu — tillar eng ko'p farq qiladigan joy. Pseudocode'da **aniq belgilang**:

```
procedure Swap(a, b)        // qiymat bo'yicha (o'zgarmaydi)
procedure Fill(ref A, n)    // havola bo'yicha (A o'zgaradi)
```

| Holat | C | C++ | Python |
|---|---|---|---|
| Qiymat bo'yicha | `int x` | `int x` | (int, str — o'zgarmas) |
| Havola/pointer | `int *a` yoki `int a[]` | `vector<int> &A` | `list` (avtomatik havola) |

**Python:** `list`, `dict`, `set` har doim **havola** orqali uzatiladi; `int`, `str`, `tuple` esa o'zgartirib bo'lmaydi.

### 9.3. Misol: massivni teskari aylantirish

```
procedure Reverse(ref A, n):
    l ← 0
    r ← n - 1
    while l < r:
        swap(A[l], A[r])
        l ← l + 1
        r ← r - 1
```

**C:**
```c
void reverse(int a[], int n) {
    int l = 0, r = n - 1;
    while (l < r) {
        int t = a[l]; a[l] = a[r]; a[r] = t;
        l++; r--;
    }
}
```

**C++:**
```cpp
void reverseArr(vector<int> &a) {
    int l = 0, r = (int)a.size() - 1;
    while (l < r) {
        swap(a[l], a[r]);
        l++; r--;
    }
}
```

**Python:**
```python
def reverse(a):
    l, r = 0, len(a) - 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
```

### 9.4. Bir nechta qiymat qaytarish

```
function MinMax(A, n):
    ...
    return (mn, mx)
```

- Python: `return mn, mx`
- C++: `pair<int,int>` yoki `tuple`
- C: pointer parametrlar yoki `struct`

### 9.5. Global o'zgaruvchilar

Iloji boricha parametr sifatida uzating. Global kerak bo'lsa (masalan, `memo`, `graph`), sarlavhada e'lon qiling:

```
GLOBAL: memo[0..n], graph
```

---

## 10. Massivlar, 2D massivlar, stringlar

### 10.1. Massiv

```
A ← array of size n                // e'lon
A ← array of size n filled with 0  // 0 bilan to'ldirilgan
A ← [1, 2, 3]                      // literal
A[i]                               // element
length(A)                          // uzunlik
```

| Pseudocode | C | C++ | Python |
|---|---|---|---|
| `A ← array of size n filled with 0` | `int a[N] = {0};` yoki `calloc` | `vector<int> a(n, 0);` | `a = [0] * n` |
| `length(A)` | `n` (alohida saqlanadi) | `a.size()` | `len(a)` |
| `append(A, x)` | (qo'lda) | `a.push_back(x);` | `a.append(x)` |

### 10.2. 2D massiv

```
G ← array of size n × m filled with 0
G[i][j] ← 1
```

| Til | Kod |
|---|---|
| C | `int g[N][M];` |
| C++ | `vector<vector<int>> g(n, vector<int>(m, 0));` |
| Python | `g = [[0] * m for _ in range(n)]` |

> **Python tuzog'i:** `[[0] * m] * n` **noto'g'ri** — barcha qatorlar bitta ob'ektga havola bo'ladi. Doim `[[0]*m for _ in range(n)]` yozing.

### 10.3. Qism massiv (subarray) va oraliqlar

```
A[l..r]       // l dan r gacha, ikkalasi kiradi
A[l..r)       // l kiradi, r kirmaydi
```

Bunda **bir uslubni tanlang va sarlavhada yozing**. Qism massivlarni nusxalash $O(r - l)$ vaqt oladi — buni yodda tuting.

### 10.4. Prefix sum (prefiks yig'indi)

```
function BuildPrefix(A, n):
    P ← array of size n+1 filled with 0
    for i ← 0 to n-1:
        P[i+1] ← P[i] + A[i]
    return P

// A[l..r) yig'indisi = P[r] - P[l]
```

Bu — yarim ochiq oraliqning qulayligi: $\text{sum}(l, r) = P[r] - P[l]$, `+1` yoki `-1` yo'q.

### 10.5. String

```
s ← "hello"
s[i]              // i-belgi
length(s)
s + t             // birlashtirish (concatenation)
substring(s, l, r)   // s[l..r)
```

| Amal | C | C++ | Python |
|---|---|---|---|
| uzunlik | `strlen(s)` | `s.size()` | `len(s)` |
| `s[i]` | `s[i]` | `s[i]` | `s[i]` |
| birlashtirish | `strcat` | `s + t` | `s + t` |
| substring `[l, r)` | `strncpy` (qo'lda) | `s.substr(l, r-l)` | `s[l:r]` |

> **Eslatma:** `substr` C++ da `(boshlanish, uzunlik)` oladi, Python slice esa `(boshlanish, tugash)`. Pseudocode'da `substring(s, l, r)` = `[l, r)` deb kelishib oling.

---

## 11. Struct / Record va murakkab ma'lumot tuzilmalari

### 11.1. Record

```
record Edge:
    to: integer
    weight: integer

e ← Edge(to = 3, weight = 7)
e.to
e.weight
```

| Til | Kod |
|---|---|
| C | `struct Edge { int to; int weight; };` |
| C++ | `struct Edge { int to, weight; };` |
| Python | `Edge = namedtuple('Edge', ['to', 'weight'])` yoki `tuple` |

### 11.2. Standart tuzilmalar

Pseudocode'da ularni **mavhum (abstract)** yozing — ichki tuzilishini emas, **amallarni** ko'rsating:

| Tuzilma | Pseudocode amallari | C++ | Python |
|---|---|---|---|
| **Stack** | `push(S, x)`, `pop(S)`, `top(S)`, `empty(S)` | `stack<T>` | `list` |
| **Queue** | `enqueue(Q, x)`, `dequeue(Q)`, `empty(Q)` | `queue<T>` | `collections.deque` |
| **Deque** | `pushFront`, `pushBack`, `popFront`, `popBack` | `deque<T>` | `collections.deque` |
| **Priority Queue (min)** | `insert(PQ, x)`, `extractMin(PQ)` | `priority_queue` (+ `greater`) | `heapq` |
| **Set** | `add(S, x)`, `contains(S, x)`, `remove(S, x)` | `set` / `unordered_set` | `set` |
| **Map / Dict** | `M[key] ← value`, `key in M` | `map` / `unordered_map` | `dict` |

> **C da** bu tuzilmalarni o'zingiz yozishingiz kerak (masalan, massiv asosida stack/queue). Shuning uchun pseudocode'ni **amallar darajasida** yozib, C implementatsiyasini alohida qilish qulay.

### 11.3. Graf tasviri

```
// Qo'shnilik ro'yxati (adjacency list)
adj[u] = u ning qo'shnilari ro'yxati

for each v in adj[u]:
    ...
```

Vaznli grafda: `adj[u]` ichida `(v, w)` juftliklar.

---

## 12. Rekursiya

### 12.1. Tuzilishi

Har bir rekursiv pseudocode 3 qismdan iborat:

```
function F(n):
    // 1. BASE CASE — to'xtash sharti
    if n ≤ 1:
        return 1
    // 2. RECURSIVE CASE — kichikroq masalaga keltirish
    // 3. KOMBINATSIYA — natijani birlashtirish
    return n × F(n - 1)
```

### 12.2. Rekursiya yozishda 4 savol

1. **Base case nima?** (eng kichik masala)
2. **Har chaqiruvda masala kichrayadimi?** (aks holda — cheksiz rekursiya)
3. **Qaytgan natijani qanday birlashtiraman?**
4. **Rekursiya chuqurligi qancha?** (Stack overflow xavfi)

### 12.3. Misol: Fibonachchi (memoization bilan)

```
GLOBAL: memo ← array of size n+1 filled with -1

function Fib(n):
    if n ≤ 1:
        return n
    if memo[n] ≠ -1:
        return memo[n]
    memo[n] ← Fib(n-1) + Fib(n-2)
    return memo[n]
```

**C:**
```c
long long memo[100];   // main da -1 bilan to'ldiring

long long fib(int n) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib(n - 1) + fib(n - 2);
}
```

**C++:**
```cpp
vector<long long> memo;

long long fib(int n) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib(n - 1) + fib(n - 2);
}
// main: memo.assign(n + 1, -1);
```

**Python:**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

### 12.4. Rekursiya chuqurligi

- **C / C++:** odatda ~$10^5$ dan ~$10^6$ gacha (stack hajmiga bog'liq).
- **Python:** standart chegara ~1000. Katta chuqurlik uchun `sys.setrecursionlimit(...)` yoki iterativ variantga o'tish kerak.

Pseudocode'da yozib qo'ying: `// chuqurlik: O(n)`.

### 12.5. Rekursiya complexity'si — Recurrence

Rekursiv pseudocode uchun **recurrence relation** yozing:

$$T(n) = T(n-1) + O(1) \Rightarrow T(n) = O(n)$$

$$T(n) = 2T(n/2) + O(n) \Rightarrow T(n) = O(n \log n)$$

$$T(n) = 2T(n-1) + O(1) \Rightarrow T(n) = O(2^n)$$

**Master theorem** ($T(n) = aT(n/b) + O(n^d)$):

| Shart | Natija |
|---|---|
| $d > \log_b a$ | $O(n^d)$ |
| $d = \log_b a$ | $O(n^d \log n)$ |
| $d < \log_b a$ | $O(n^{\log_b a})$ |

---

## 13. Invariant, precondition, postcondition

Bu — pseudocode'ni **professional darajaga** ko'taradigan qism.

### 13.1. Tushunchalar

| Atama | Ma'nosi |
|---|---|
| **Precondition** | Funksiya chaqirilishidan **oldin** to'g'ri bo'lishi shart bo'lgan shart |
| **Postcondition** | Funksiya tugagach **kafolatlanadigan** shart |
| **Loop invariant** | Sikl **har bir iteratsiya boshida** to'g'ri bo'ladigan shart |

### 13.2. Misol: massivdagi maksimum

```
function MaxElement(A, n):
    // Precondition: n ≥ 1
    mx ← A[0]
    for i ← 1 to n-1:
        // Invariant: mx = max(A[0..i-1])
        if A[i] > mx:
            mx ← A[i]
    // Postcondition: mx = max(A[0..n-1])
    return mx
```

### 13.3. Invariant isboti — 3 qadam

1. **Initialization (boshlanish):** sikldan oldin invariant to'g'rimi?
   `i = 1` da `mx = A[0] = max(A[0..0])` ✓
2. **Maintenance (saqlanish):** iteratsiya invariantni saqlaydimi?
   Agar `mx = max(A[0..i-1])` bo'lsa, `A[i]` bilan solishtirgach `mx = max(A[0..i])` ✓
3. **Termination (tugash):** sikl tugaganda invariant nima beradi?
   `i = n` da `mx = max(A[0..n-1])` — kerakli natija ✓

### 13.4. Nima uchun bu muhim?

Musobaqada "nega ishlaydi?" degan savolga javob berolmasangiz, algoritmni **ishonchsiz** hisoblang. Invariantni yozish sizni:
- off-by-one xatolardan,
- noto'g'ri chegara shartlaridan
saqlaydi.

---

## 14. Complexity analysis pseudocode'dan

Pseudocode'dan complexity'ni **mexanik** hisoblash mumkin.

### 14.1. Qoidalar

| Konstruksiya | Vaqt |
|---|---|
| Oddiy amal (`+`, `←`, `A[i]`, taqqoslash) | $O(1)$ |
| Ketma-ket bloklar | **Qo'shiladi** |
| `if/else` | Eng katta tarmoq (worst case) |
| Sikl | (iteratsiyalar soni) × (bir iteratsiya narxi) |
| Ichma-ich sikllar | **Ko'paytiriladi** |
| Funksiya chaqiruvi | Funksiyaning o'z complexity'si |

### 14.2. Namunalar

**Bitta sikl:**
```
for i ← 0 to n-1:      // n marta
    x ← x + A[i]       // O(1)
```
$\Rightarrow O(n)$

**Ichma-ich sikl:**
```
for i ← 0 to n-1:
    for j ← 0 to n-1:
        ...            // O(1)
```
$\Rightarrow O(n^2)$

**Uchburchak sikl:**
```
for i ← 0 to n-1:
    for j ← i+1 to n-1:
        ...
```
$\sum_{i=0}^{n-1}(n-1-i) = \frac{n(n-1)}{2} \Rightarrow O(n^2)$

**Har iteratsiyada yarmiga bo'linish:**
```
while n > 1:
    n ← ⌊n / 2⌋
```
$\Rightarrow O(\log n)$

**Garmonik qator (sieve):**
```
for i ← 1 to n:
    for j ← i to n step i:
        ...
```
$\sum_{i=1}^{n} \frac{n}{i} = n \cdot H_n \Rightarrow O(n \log n)$

**Ikkita pointer (two pointers):**
```
l ← 0
for r ← 0 to n-1:
    while l < r and shart:
        l ← l + 1
```
`l` va `r` har biri ko'pi bilan $n$ marta oshadi $\Rightarrow$ **amortizatsiyalangan** $O(n)$ (ichki `while` bo'lishiga qaramay).

### 14.3. Space complexity

- Qo'shimcha massivlar, rekursiya stek chuqurligi, xesh jadvallar — hammasi hisobga olinadi.
- Rekursiya chuqurligi $d$ bo'lsa, stek xotirasi $O(d)$.

### 14.4. Asimptotik belgilar

| Belgi | Ma'nosi |
|---|---|
| $O(f)$ | yuqori chegara (worst-case uchun ko'p ishlatiladi) |
| $\Omega(f)$ | pastki chegara |
| $\Theta(f)$ | aniq chegara |

---

## 15. Pseudocode → C / C++ / Python tarjima jadvali

Bu — **yagona ma'lumotnoma jadval**. Uni chop etib qo'yishingiz mumkin.

| Pseudocode | C | C++ | Python |
|---|---|---|---|
| `x ← 5` | `x = 5;` | `x = 5;` | `x = 5` |
| `a ↔ b` | `t=a; a=b; b=t;` | `swap(a,b);` | `a, b = b, a` |
| `if c: ... else: ...` | `if (c) {...} else {...}` | `if (c) {...} else {...}` | `if c: ... else: ...` |
| `for i ← 0 to n-1` | `for(int i=0;i<n;i++)` | `for(int i=0;i<n;i++)` | `for i in range(n):` |
| `for i ← n-1 down to 0` | `for(int i=n-1;i>=0;i--)` | `for(int i=n-1;i>=0;i--)` | `for i in range(n-1,-1,-1):` |
| `while c:` | `while (c) {...}` | `while (c) {...}` | `while c:` |
| `repeat ... until c` | `do{...}while(!c);` | `do{...}while(!c);` | `while True: ...; if c: break` |
| `⌊a / b⌋` | `a / b` | `a / b` | `a // b` |
| `a mod b` | `a % b` | `a % b` | `a % b` |
| `a^b` | `pow` (double!) / sikl | `pow` (double!) / sikl | `a ** b` |
| `a AND b` | `a & b` | `a & b` | `a & b` |
| `not c` | `!c` | `!c` | `not c` |
| `c1 and c2` | `c1 && c2` | `c1 && c2` | `c1 and c2` |
| `A ← array of size n filled with 0` | `int A[N]={0};` | `vector<int> A(n,0);` | `A = [0]*n` |
| `length(A)` | (`n` alohida) | `A.size()` | `len(A)` |
| `append(A, x)` | — | `A.push_back(x);` | `A.append(x)` |
| `INF` | `INT_MAX` / `1e18` | `INT_MAX` / `LLONG_MAX` | `float('inf')` |
| `NIL` | `NULL` / `-1` | `nullptr` / `-1` | `None` |
| `return (a, b)` | struct / pointer | `pair` / `tuple` | `return a, b` |

### Tarjimada ehtiyot bo'lish kerak bo'lgan joylar

| Muammo | Tavsif |
|---|---|
| **Overflow** | C/C++ `int` ~$2 \cdot 10^9$ gacha. Yig'indi/ko'paytma katta bo'lsa `long long`. Python'da yo'q. |
| **`pow` aniqligi** | C/C++ `pow` `double` qaytaradi; katta butun sonlar uchun xato beradi. Sikl bilan yozing. |
| **Manfiy bo'lish/qoldiq** | C/C++ va Python farq qiladi (4-bo'lim). |
| **Massiv chegarasi** | C/C++ da chegaradan chiqish — undefined behavior; Python'da `IndexError`. Manfiy indeks Python'da oxirdan sanaydi! |
| **Python tezligi** | Bir xil $O(n)$ bo'lsa ham, Python C++ dan ~50× sekin bo'lishi mumkin. |
| **C da dinamik massiv** | `malloc/free` yoki oldindan katta `N`. |

---

## 16. Klassik andozalar (templates)

Quyidagi qolipni yodlab olsangiz, ko'p masalada pseudocode'ni tezroq yozasiz.

### 16.1. Chiziqli qidiruv (Linear Search)

```
function LinearSearch(A, n, x):
    for i ← 0 to n-1:
        if A[i] = x:
            return i
    return -1
```
$O(n)$ vaqt, $O(1)$ xotira.

### 16.2. Ikkita pointer (Two Pointers) — saralangan massivda juft yig'indisi

```
function TwoSum(A, n, target):       // A saralangan
    l ← 0
    r ← n - 1
    while l < r:
        s ← A[l] + A[r]
        if s = target:
            return (l, r)
        else if s < target:
            l ← l + 1
        else:
            r ← r - 1
    return NIL
```
$O(n)$.

### 16.3. Sliding window — uzunligi $k$ bo'lgan oynaning maksimal yig'indisi

```
function MaxWindowSum(A, n, k):
    s ← sum(A[0..k-1])
    best ← s
    for i ← k to n-1:
        s ← s + A[i] - A[i-k]
        best ← max(best, s)
    return best
```
$O(n)$.

### 16.4. Binary search (javob ustida)

```
function BinarySearchAnswer(lo, hi):
    // Invariant: check(lo) = false, check(hi) = true
    while hi - lo > 1:
        mid ← lo + ⌊(hi - lo) / 2⌋
        if check(mid):
            hi ← mid
        else:
            lo ← mid
    return hi
```
$O(\log(\text{hi} - \text{lo}) \cdot T_{\text{check}})$.

### 16.5. DFS (rekursiv)

```
procedure DFS(u):
    visited[u] ← true
    for each v in adj[u]:
        if not visited[v]:
            DFS(v)
```
$O(V + E)$.

### 16.6. BFS

```
function BFS(s):
    dist ← array of size V filled with -1
    dist[s] ← 0
    Q ← empty queue
    enqueue(Q, s)
    while not empty(Q):
        u ← dequeue(Q)
        for each v in adj[u]:
            if dist[v] = -1:
                dist[v] ← dist[u] + 1
                enqueue(Q, v)
    return dist
```
$O(V + E)$.

### 16.7. DP — 1D

```
// dp[i] = i-holat uchun javob
dp[0] ← base
for i ← 1 to n:
    dp[i] ← kombinatsiya(dp[i-1], dp[i-2], ...)
return dp[n]
```

DP pseudocode'ida doim 4 narsani yozing:
1. **Holat (state):** `dp[i]` nimani bildiradi?
2. **Bazaviy holat:** `dp[0] = ?`
3. **O'tish (transition):** `dp[i]` qanday hisoblanadi?
4. **Javob:** qaysi `dp[...]` javob?

### 16.8. Greedy (intervallar tanlash)

```
function MaxNonOverlapping(intervals, n):
    sort intervals by end time ascending
    count ← 0
    lastEnd ← -∞
    for each (s, e) in intervals:
        if s ≥ lastEnd:
            count ← count + 1
            lastEnd ← e
    return count
```
$O(n \log n)$ (saralash hisobiga).

### 16.9. Modulli arifmetika

```
MOD ← 1_000_000_007

function ModPow(base, exp, MOD):
    result ← 1
    base ← base mod MOD
    while exp > 0:
        if exp AND 1 = 1:
            result ← (result × base) mod MOD
        base ← (base × base) mod MOD
        exp ← exp >> 1
    return result
```
$O(\log \text{exp})$. C/C++ da `long long` shart: `(result * base)` $\approx 10^{18}$ ga yetadi.

---

## 17. To'liq misol: Binary Search

### 17.1. Masala

Saralangan (o'sish tartibida) `A[0..n-1]` massivda `x` sonining **birinchi** uchragan indeksini toping. Yo'q bo'lsa `-1`.

- $1 \le n \le 2 \cdot 10^5$
- Vaqt: 1 soniya

### 17.2. Qog'ozda tahlil

**Cheklov:** $n = 2 \cdot 10^5$ → $O(n)$ ham o'tadi, lekin saralanganlikdan foydalanib $O(\log n)$ qilamiz.

**Misol:** `A = [1, 3, 3, 3, 5, 8]`, `x = 3` → javob `1`.

**G'oya:** "birinchi `i` topamiki, `A[i] ≥ x`" — bu lower bound. Keyin `A[i] = x` ekanini tekshiramiz.

**Invariant:**
- `A[0..lo)` dagi barcha elementlar `< x`
- `A[hi..n)` dagi barcha elementlar `≥ x`

Boshida `lo = 0`, `hi = n` — ikkala oraliq bo'sh, invariant to'g'ri.

### 17.3. Pseudocode

```
ALGORITHM: FirstOccurrence
INPUT:  A[0..n-1] saralangan (o'sish), n ≥ 1, x
OUTPUT: x ning birinchi indeksi yoki -1
TIME:   O(log n)
SPACE:  O(1)

function FirstOccurrence(A, n, x):
    lo ← 0
    hi ← n                       // qidiruv oralig'i: [lo, hi)
    while lo < hi:
        // Invariant: A[0..lo) < x  va  A[hi..n) ≥ x
        mid ← lo + ⌊(hi - lo) / 2⌋
        if A[mid] < x:
            lo ← mid + 1
        else:
            hi ← mid
    // lo = hi = birinchi indeks, bunda A[i] ≥ x
    if lo < n and A[lo] = x:
        return lo
    return -1
```

### 17.4. Trace

`A = [1, 3, 3, 3, 5, 8]`, `x = 3`, `n = 6`:

| qadam | lo | hi | mid | A[mid] | harakat |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 3 | `3 < 3`? yo'q → `hi = 3` |
| 2 | 0 | 3 | 1 | 3 | `3 < 3`? yo'q → `hi = 1` |
| 3 | 0 | 1 | 0 | 1 | `1 < 3`? ha → `lo = 1` |
| — | 1 | 1 | — | — | sikl tugadi |

`lo = 1`, `A[1] = 3 = x` → javob `1` ✓

### 17.5. Complexity

Har iteratsiyada oraliq kamida yarmiga kamayadi: $n \to n/2 \to n/4 \to \dots \to 1$. Iteratsiyalar soni $\lceil \log_2 n \rceil + 1$.

$$T(n) = O(\log n), \quad S(n) = O(1)$$

### 17.6. Implementatsiyalar

**C:**
```c
#include <stdio.h>

int first_occurrence(const int a[], int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    if (lo < n && a[lo] == x) return lo;
    return -1;
}

int main(void) {
    int a[] = {1, 3, 3, 3, 5, 8};
    printf("%d\n", first_occurrence(a, 6, 3));   // 1
    return 0;
}
```

**C++:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int firstOccurrence(const vector<int> &a, int x) {
    int lo = 0, hi = (int)a.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    if (lo < (int)a.size() && a[lo] == x) return lo;
    return -1;
}

int main() {
    vector<int> a = {1, 3, 3, 3, 5, 8};
    cout << firstOccurrence(a, 3) << "\n";   // 1
    return 0;
}
```

**Python:**
```python
def first_occurrence(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    if lo < len(a) and a[lo] == x:
        return lo
    return -1

print(first_occurrence([1, 3, 3, 3, 5, 8], 3))   # 1
```

### 17.7. Nima uchun `mid = lo + (hi - lo) / 2`?

`(lo + hi) / 2` da `lo + hi` `int` chegarasidan oshib ketishi (overflow) mumkin. `lo + (hi - lo)/2` xavfsiz. Python'da bu muammo yo'q, lekin bir xil odat bo'lgani yaxshi.

### 17.8. Edge case'lar

| Holat | Kutilgan |
|---|---|
| `n = 1`, `A=[5]`, `x=5` | `0` |
| `n = 1`, `A=[5]`, `x=3` | `-1` |
| `x` barcha elementlardan kichik | `-1` (`lo = 0`, `A[0] ≠ x`) |
| `x` barcha elementlardan katta | `-1` (`lo = n`, `lo < n` yolg'on) |
| Barcha elementlar `x` ga teng | `0` |

---

## 18. To'liq misol: 0/1 Knapsack (DP)

### 18.1. Masala

$n$ ta buyum, har birining og'irligi $w_i$ va qiymati $v_i$. Ryukzak sig'imi $W$. Umumiy og'irlik $W$ dan oshmasin, qiymat maksimal bo'lsin. Har buyum bir marta olinadi.

- $n \le 100$, $W \le 10^4$

### 18.2. Qog'ozda tahlil

**Cheklov:** $n \cdot W = 10^6$ → $O(nW)$ mos.

**Holat:** `dp[i][j]` = dastlabki `i` ta buyumdan foydalanib, sig'im `j` bo'lganda maksimal qiymat.

**O'tish:** `i`-buyum uchun ikki tanlov:
- Olmaymiz: `dp[i-1][j]`
- Olamiz (agar `w[i-1] ≤ j`): `dp[i-1][j - w[i-1]] + v[i-1]`

$$dp[i][j] = \max\bigl(dp[i-1][j],\; dp[i-1][j - w_{i-1}] + v_{i-1}\bigr)$$

**Baza:** `dp[0][j] = 0` (buyum yo'q → qiymat 0).

**Javob:** `dp[n][W]`.

### 18.3. Pseudocode

```
ALGORITHM: Knapsack01
INPUT:  w[0..n-1], v[0..n-1], n, W
OUTPUT: maksimal umumiy qiymat
TIME:   O(n × W)
SPACE:  O(n × W)   (1D ga optimallashtirish mumkin: O(W))

function Knapsack(w, v, n, W):
    dp ← array of size (n+1) × (W+1) filled with 0
    for i ← 1 to n:
        for j ← 0 to W:
            dp[i][j] ← dp[i-1][j]                       // olmaymiz
            if w[i-1] ≤ j:
                take ← dp[i-1][j - w[i-1]] + v[i-1]     // olamiz
                dp[i][j] ← max(dp[i][j], take)
    return dp[n][W]
```

### 18.4. Xotirani optimallashtirish (1D)

`dp[i]` faqat `dp[i-1]` ga bog'liq, shuning uchun bitta massiv yetadi. **`j` ni kamayish tartibida** yuring (aks holda buyum ikki marta olinadi):

```
function Knapsack1D(w, v, n, W):
    dp ← array of size (W+1) filled with 0
    for i ← 0 to n-1:
        for j ← W down to w[i]:
            dp[j] ← max(dp[j], dp[j - w[i]] + v[i])
    return dp[W]
```

$S(n) = O(W)$.

### 18.5. Implementatsiyalar (1D variant)

**C:**
```c
#include <stdio.h>
#include <string.h>

int knapsack(const int w[], const int v[], int n, int W) {
    static int dp[10001];
    memset(dp, 0, sizeof(dp));
    for (int i = 0; i < n; i++)
        for (int j = W; j >= w[i]; j--)
            if (dp[j - w[i]] + v[i] > dp[j])
                dp[j] = dp[j - w[i]] + v[i];
    return dp[W];
}

int main(void) {
    int w[] = {1, 3, 4, 5};
    int v[] = {1, 4, 5, 7};
    printf("%d\n", knapsack(w, v, 4, 7));   // 9
    return 0;
}
```

**C++:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int knapsack(const vector<int> &w, const vector<int> &v, int W) {
    int n = w.size();
    vector<int> dp(W + 1, 0);
    for (int i = 0; i < n; i++)
        for (int j = W; j >= w[i]; j--)
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
    return dp[W];
}

int main() {
    cout << knapsack({1, 3, 4, 5}, {1, 4, 5, 7}, 7) << "\n";   // 9
}
```

**Python:**
```python
def knapsack(w, v, W):
    dp = [0] * (W + 1)
    for wi, vi in zip(w, v):
        for j in range(W, wi - 1, -1):
            dp[j] = max(dp[j], dp[j - wi] + vi)
    return dp[W]

print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))   # 9
```

**Tekshiruv:** `W = 7` da eng yaxshi tanlov — og'irligi 3 va 4 bo'lgan buyumlar (qiymat $4 + 5 = 9$) ✓

---

## 19. To'liq misol: BFS (eng qisqa yo'l, vaznsiz graf)

### 19.1. Masala

$N$ ta uchli vaznsiz yo'naltirilmagan graf berilgan. `s` uchidan barcha uchlargacha eng qisqa masofani (qirralar soni) toping. Yetib bo'lmasa `-1`.

- $N, M \le 2 \cdot 10^5$

### 19.2. Qog'ozda tahlil

Vaznsiz graf + eng qisqa yo'l → **BFS**. Har bir uch bir marta navbatga tushadi → $O(N + M)$.

**Invariant:** navbatdagi uchlar masofasi bo'yicha o'sish tartibida joylashgan va farqi ko'pi bilan 1.

### 19.3. Pseudocode

```
ALGORITHM: BFS-ShortestPath
INPUT:  adj[0..N-1] (qo'shnilik ro'yxati), s
OUTPUT: dist[0..N-1]
TIME:   O(N + M)
SPACE:  O(N + M)

function BFS(adj, N, s):
    dist ← array of size N filled with -1
    dist[s] ← 0
    Q ← empty queue
    enqueue(Q, s)
    while not empty(Q):
        u ← dequeue(Q)
        for each v in adj[u]:
            if dist[v] = -1:                // hali ko'rilmagan
                dist[v] ← dist[u] + 1
                enqueue(Q, v)
    return dist
```

### 19.4. Implementatsiyalar

**C** (massiv asosidagi navbat va qo'shnilik ro'yxati — "forward star"):
```c
#include <stdio.h>
#include <string.h>

#define MAXN 200005
#define MAXM 400005

int head[MAXN], nxt[MAXM], to[MAXM], cnt = 0;
int dist[MAXN], queue_[MAXN];

void add_edge(int u, int v) {
    to[cnt] = v; nxt[cnt] = head[u]; head[u] = cnt++;
}

void bfs(int n, int s) {
    for (int i = 0; i < n; i++) dist[i] = -1;
    int qh = 0, qt = 0;
    dist[s] = 0;
    queue_[qt++] = s;
    while (qh < qt) {
        int u = queue_[qh++];
        for (int e = head[u]; e != -1; e = nxt[e]) {
            int v = to[e];
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                queue_[qt++] = v;
            }
        }
    }
}

int main(void) {
    int n, m, s;
    scanf("%d %d %d", &n, &m, &s);
    memset(head, -1, sizeof(head));
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        add_edge(u, v);
        add_edge(v, u);
    }
    bfs(n, s);
    for (int i = 0; i < n; i++) printf("%d ", dist[i]);
    printf("\n");
    return 0;
}
```

**C++:**
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> bfs(const vector<vector<int>> &adj, int s) {
    int n = adj.size();
    vector<int> dist(n, -1);
    queue<int> q;
    dist[s] = 0;
    q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, s;
    cin >> n >> m >> s;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (int d : bfs(adj, s)) cout << d << " ";
    cout << "\n";
}
```

**Python:**
```python
import sys
from collections import deque

def bfs(adj, s):
    dist = [-1] * len(adj)
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def main():
    data = sys.stdin.read().split()
    n, m, s = int(data[0]), int(data[1]), int(data[2])
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = int(data[3 + 2 * i]), int(data[4 + 2 * i])
        adj[u].append(v)
        adj[v].append(u)
    print(*bfs(adj, s))

main()
```

> Python'da `list.pop(0)` $O(n)$ — navbat uchun **doim** `deque` ishlating.

---

## 20. Ko'p uchraydigan xatolar

### 20.1. Pseudocode xatolari

| Xato | Misol | Tuzatish |
|---|---|---|
| **Noaniq qadam** | "eng yaxshisini tanla" | Qanday tanlanishini aniq yozing |
| **Til-xos tafsilot** | `vector<int>::iterator it` | "elementlar bo'yicha yur" |
| **Konventsiyani aralashtirish** | 0-based va 1-based | Boshida bir marta e'lon qiling |
| **Chegaralar noaniq** | `for i in 1..n` (kiradimi?) | `to` = ikkala chegara kiradi |
| **Base case yo'q** | rekursiyada | Doim birinchi yozing |
| **O'zgaruvchi e'lon qilinmagan** | `sum` ishlatilgan, lekin `sum ← 0` yo'q | Inisializatsiyani yozing |
| **Edge case unutilgan** | `n = 0`, `n = 1` | Precondition yozing |
| **Juda batafsil** | har bir `i++` ni yozish | Mantiq darajasida qoling |
| **Juda yuzaki** | "saralab, javobni chiqar" | Qanday saralash, qaysi kalit? |

### 20.2. Pseudocode'dan kodga o'tishdagi xatolar

| Xato | Sabab | Tuzatish |
|---|---|---|
| **Off-by-one** | `to` va `range` farqi | Jadvaldan foydalaning (8.1) |
| **Integer overflow** | C/C++ `int` | `long long` (izohni pseudocode'ga yozing) |
| **Integer division** | Python `/` real qaytaradi | Python'da `//` |
| **Aliasing** | Python: `b = a` nusxa emas | `b = a[:]` yoki `list(a)` |
| **2D massiv** | `[[0]*m]*n` | `[[0]*m for _ in range(n)]` |
| **Initialization** | C da lokal massiv chiqindi qiymat | `= {0}` yoki `memset` |
| **Rekursiya chegarasi** | Python 1000 | `setrecursionlimit` yoki iterativ |
| **Sekin I/O** | `cin` sinxronlashuvi, `input()` | Tez I/O |

### 20.3. Ishlash tezligi bo'yicha "yashirin" narxlar

Pseudocode'da $O(1)$ ko'ringan amal aslida qimmat bo'lishi mumkin:

| Pseudocode | Haqiqiy narx |
|---|---|
| `B ← A` (massiv nusxasi) | $O(n)$ |
| `s ← s + c` (string qo'shish sikl ichida) | $O(n)$ har safar → jami $O(n^2)$ |
| `substring(s, l, r)` | $O(r - l)$ |
| `x in list` (Python) | $O(n)$ |
| `list.pop(0)` (Python) | $O(n)$ |
| `insert(A, 0, x)` | $O(n)$ |

> Pseudocode yozayotganda "bu amal necha qadam?" deb so'rab turing.

---

## 21. Tekshiruv ro'yxati (checklist)

Pseudocode tayyor bo'lgach, quyidagilarni tekshiring:

**Spetsifikatsiya**
- [ ] `INPUT`, `OUTPUT` aniq yozilganmi?
- [ ] Precondition'lar (`n ≥ 1`, saralangan, ...) bormi?
- [ ] Indeks va oraliq konventsiyasi e'lon qilinganmi?

**Mantiq**
- [ ] Barcha o'zgaruvchilar inisializatsiya qilinganmi?
- [ ] Har bir sikl uchun invariant va tugash sharti aniqmi?
- [ ] Rekursiyada base case bormi va masala kichrayyaptimi?
- [ ] Barcha tarmoqlar (`if/else`) qamrab olinganmi?

**Tekshiruv**
- [ ] Kamida bitta misolda **trace** qilinganmi?
- [ ] Edge case'lar: bo'sh, bitta element, barchasi bir xil, eng katta $n$?
- [ ] Javob qaytarilishi barcha yo'llarda ta'minlanganmi?

**Complexity**
- [ ] Vaqt va xotira hisoblanganmi?
- [ ] Cheklovlarga sig'adimi (2-bo'limdagi jadval)?
- [ ] Overflow xavfi bormi? (`64-bit` izohi)

**Tarjima**
- [ ] Til-xos tuzoqlar (15-bo'lim) ko'rib chiqilganmi?

---

## 22. Mashqlar va yechimlar

Avval o'zingiz pseudocode yozing, keyin yechim bilan solishtiring.

### Mashq 1 (oson): Massiv elementlari yig'indisi va o'rtachasi

**Masala:** `A[0..n-1]` berilgan. Yig'indi va o'rtachani (real) toping.

<details>
<summary>Yechim</summary>

```
function SumAvg(A, n):
    // Precondition: n ≥ 1
    s ← 0                        // 64-bit
    for i ← 0 to n-1:
        s ← s + A[i]
    avg ← s / n                  // real bo'lish
    return (s, avg)
```
$O(n)$.
</details>

### Mashq 2 (oson): Palindrom tekshirish

**Masala:** `s` string palindrommi?

<details>
<summary>Yechim</summary>

```
function IsPalindrome(s):
    l ← 0
    r ← length(s) - 1
    while l < r:
        if s[l] ≠ s[r]:
            return false
        l ← l + 1
        r ← r - 1
    return true
```
$O(n)$, $O(1)$ xotira. Bo'sh string va bitta belgi uchun `true`.
</details>

### Mashq 3 (o'rta): Ikkinchi eng katta element

**Masala:** Massivdagi ikkinchi eng katta **farqli** elementni toping (yo'q bo'lsa `NIL`).

<details>
<summary>Yechim</summary>

```
function SecondMax(A, n):
    first ← -∞
    second ← -∞
    for i ← 0 to n-1:
        if A[i] > first:
            second ← first
            first ← A[i]
        else if A[i] < first and A[i] > second:
            second ← A[i]
    if second = -∞:
        return NIL
    return second
```
`A[i] < first` sharti dublikatlarni chetlab o'tadi. $O(n)$, bitta o'tish.
</details>

### Mashq 4 (o'rta): Ketma-ket eng uzun o'suvchi qism (subarray)

**Masala:** `A` da ketma-ket joylashgan, qat'iy o'suvchi eng uzun qism massiv uzunligini toping.

<details>
<summary>Yechim</summary>

```
function LongestIncreasingRun(A, n):
    // Precondition: n ≥ 1
    best ← 1
    cur ← 1
    for i ← 1 to n-1:
        // Invariant: cur = A[..i-1] oxiridagi o'suvchi run uzunligi
        if A[i] > A[i-1]:
            cur ← cur + 1
        else:
            cur ← 1
        best ← max(best, cur)
    return best
```
$O(n)$.
</details>

### Mashq 5 (o'rta): Sonning tub ekanini tekshirish

**Masala:** $n \le 10^{12}$ soni tubmi?

<details>
<summary>Yechim</summary>

```
function IsPrime(n):              // n: 64-bit
    if n < 2:
        return false
    d ← 2
    while d × d ≤ n:              // d×d ≤ n: 64-bit
        if n mod d = 0:
            return false
        d ← d + 1
    return true
```
$O(\sqrt{n})$: $\sqrt{10^{12}} = 10^6$ — o'tadi. `d * d` uchun `long long` shart.
</details>

### Mashq 6 (qiyin): Ikkita saralangan massivni birlashtirish (merge)

<details>
<summary>Yechim</summary>

```
function Merge(A, n, B, m):
    C ← array of size n + m
    i ← 0
    j ← 0
    k ← 0
    while i < n and j < m:
        if A[i] ≤ B[j]:
            C[k] ← A[i]; i ← i + 1
        else:
            C[k] ← B[j]; j ← j + 1
        k ← k + 1
    while i < n:
        C[k] ← A[i]; i ← i + 1; k ← k + 1
    while j < m:
        C[k] ← B[j]; j ← j + 1; k ← k + 1
    return C
```
$O(n + m)$. `A[i] ≤ B[j]` (qat'iy emas) — barqarorlik (stability) uchun.
</details>

### Mashq 7 (qiyin): Eng uzun umumiy qism ketma-ketlik (LCS)

**Masala:** `s` va `t` ning eng uzun umumiy qism ketma-ketligi uzunligi.

<details>
<summary>Yechim</summary>

**Holat:** `dp[i][j]` = `s[0..i)` va `t[0..j)` ning LCS uzunligi.

**O'tish:**
- `s[i-1] = t[j-1]` bo'lsa: `dp[i][j] = dp[i-1][j-1] + 1`
- Aks holda: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

**Baza:** `dp[0][j] = dp[i][0] = 0`.

```
function LCS(s, t):
    n ← length(s)
    m ← length(t)
    dp ← array of size (n+1) × (m+1) filled with 0
    for i ← 1 to n:
        for j ← 1 to m:
            if s[i-1] = t[j-1]:
                dp[i][j] ← dp[i-1][j-1] + 1
            else:
                dp[i][j] ← max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]
```
$O(nm)$ vaqt va xotira.
</details>

### Mashq 8 (mustaqil): O'zingiz sinab ko'ring

Har bir masala uchun **to'liq jarayon** (2-bo'lim) bo'yicha ishlang: cheklov → misol → g'oya → pseudocode → trace → complexity → 3 til.

1. Massivda ikkita element yig'indisi $K$ ga teng bo'lgan juftliklar soni (saralanmagan massiv; `hash` bilan).
2. Qavslar ketma-ketligi to'g'ri joylashganmi (`()[]{}`)? (stack)
3. Grafda bog'langan komponentlar soni. (DFS/BFS)
4. Eng katta o'suvchi qism ketma-ketlik (LIS) $O(n \log n)$. (binary search + DP)
5. $[1, n]$ oralig'idagi barcha tub sonlar (Sieve of Eratosthenes).

---

## Yakuniy maslahatlar

1. **Bir uslubni tanlang va unga sodiq qoling.** Barqarorlik — tezlik demak.
2. **Doim trace qiling.** Kichik misolda qo'lda bajarilmagan pseudocode — ishonchsiz.
3. **Invariant yozing.** Ayniqsa `binary search`, `two pointers`, `DP` da.
4. **Sarlavha (INPUT/OUTPUT/TIME/SPACE) yozishni odat qiling.** Bu fikrni tartibga soladi.
5. **Til tuzoqlarini bilib oling** (15-bo'lim) — bu pseudocode'dan kodga o'tishdagi xatolarning asosiy manbai.
6. **Har bir yechimdan keyin savol bering:** "Pseudocode'im shu masalaning barcha edge case'larini qamrab olganmi?"
7. **Kunlik amaliyot:** har kuni 1 ta masalani to'liq jarayon bilan (pseudocode → 3 til) yeching. 30 kundan keyin pseudocode yozish avtomatik bo'lib qoladi.

> **Eslatma:** mukammal pseudocode — eng qisqa emas, balki **boshqa dasturchi (yoki kelajakdagi o'zingiz) hech qanday savolsiz kodga o'gira oladigan** pseudocode.
