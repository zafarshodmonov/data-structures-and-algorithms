# Pseudocode Cheat Sheet (Yagona standart)

> **Qoida:** bir tushuncha = bitta yozuv. Uslubni o'zgartirmang.

---

## 1. Sarlavha (majburiy)

```
ALGORITHM: Nomi
INPUT:  ... (turi, cheklovlar, precondition)
OUTPUT: ...
TIME:   O(...)
SPACE:  O(...)
```

## 2. Indeks va oraliq

| Nima | Qoida |
|---|---|
| Indekslash | **0-based** |
| `for i = a to b` | `a` va `b` **ikkalasi kiradi** |
| `A[l..r]` | ikkalasi kiradi |
| `A[l..r)` | `r` kirmaydi (binary search, prefix sum) |

## 3. Belgilar

| Nima | Yozuv |
|---|---|
| Qiymat berish | `x = 5` |
| Tenglik / teng emas | `==`  `!=` |
| Taqqoslash | `<  >  <=  >=` |
| Mantiqiy | `and  or  not` |
| Bit | `AND  OR  XOR  <<  >>` |
| Real bo'lish | `a / b` |
| Butun bo'lish | `a div b` |
| Qoldiq | `a mod b` |
| Daraja | `a ^ b` |
| Yaxlitlash | `floor(x)`  `ceil(x)` |
| Almashtirish | `swap(a, b)` |
| Cheksizlik / bo'sh | `INF`  `NIL` |
| Mantiqiy qiymat | `true`  `false` |
| Izoh | `// izoh` |

## 4. Bloklar

- Indentatsiya: **4 ta bo'sh joy**, qator oxirida `:`
- Kalit so'zlar **kichik harfda**: `if else for while return`
- Faqat `ALGORITHM INPUT OUTPUT TIME SPACE GLOBAL` — BOSH HARFda
- Bo'sh blok: `...` (`pass` emas)

## 5. Shart

```
if shart:
    ...
else if shart:
    ...
else:
    ...
```

## 6. Sikllar (faqat shu)

```
for i = a to b:
for i = a down to b:
for i = a to b step k:
for each x in A:
while shart:
repeat:
    ...
until shart

break
continue
```

`range(...)` yozmang.

## 7. Funksiya

```
function Nomi(a, b):          // qiymat qaytaradi
    return natija

procedure Nomi(ref A, n):     // qaytarmaydi
    ...
```

- Funksiya: `PascalCase` (`MaxElement`)
- O'zgaruvchi: `camelCase` yoki qisqa (`mx`, `lo`, `bestSum`)
- O'zgartiriladigan parametr: `ref`
- `sum`, `max`, `len`, `list` kabi o'rnatilgan nomlarni ishlatmang
- Bir nechta qiymat: `return (a, b)`

## 8. Massiv va tuzilmalar

```
A = array of size n filled with 0
A = [1, 2, 3]
B = array of size n × m filled with 0      // B[i][j]
length(A)
append(A, x)
```

| Tuzilma | Amallar |
|---|---|
| Stack | `push  pop  top  empty` |
| Queue | `enqueue  dequeue  empty` |
| Priority queue | `insert  extractMin` |
| Set | `add  contains  remove` |
| Map | `M[key] = value`, `key in M` |
| Record | `record Edge: to, weight` → `e.to` |

## 9. I/O

```
read n
read A[0..n-1]
print x
```

## 10. Tur va overflow

```
s = 0                       // 64-bit
mid = lo + (hi - lo) div 2
```

## 11. Uch kafolat

```
// Precondition:  n >= 1
// Invariant:     mx == max(A[0..i-1])
// Postcondition: mx == max(A[0..n-1])
```

## 12. Abstraksiya

1. Bir qator = bitta harakat.
2. Til-xos narsa yozilmaydi (`iterator`, `comprehension`, `pass`).
3. Noaniq ibora yo'q ("eng yaxshisini tanla").
4. O'zgaruvchi ishlatilishidan **oldin** inisializatsiya qilinadi.

---

## Yagona jarayon (8 qadam)

| # | Qadam | Nima qilinadi |
|---|---|---|
| 1 | Tushunish | INPUT, OUTPUT, cheklovlar |
| 2 | Qo'lda misol | kichik misol + edge case (n=1, bo'sh, hammasi teng) |
| 3 | G'oya | greedy / DP / BFS / binary search / ... |
| 4 | Pseudocode | shu standartda, sarlavha bilan |
| 5 | Trace | jadval: qadam \| o'zgaruvchilar |
| 6 | Complexity | cheklovga sig'adimi |
| 7 | Tarjima | C, C++, Python |
| 8 | Test | misol + edge case |

## Cheklov → complexity

| $n$ | Ruxsat etilgan |
|---|---|
| $\le 10$ | $O(n!)$ |
| $\le 20$ | $O(2^n \cdot n)$ |
| $\le 500$ | $O(n^3)$ |
| $\le 5000$ | $O(n^2)$ |
| $\le 10^5 - 10^6$ | $O(n \log n)$ |
| $\le 10^7 - 10^8$ | $O(n)$ |
| $\le 10^{18}$ | $O(\log n)$ |

---

## Shablon

```
ALGORITHM: Nomi
INPUT:  ...
OUTPUT: ...
TIME:   O(...)
SPACE:  O(...)

function Nomi(params):
    // Precondition: ...
    x = boshlang'ich qiymat
    for i = 0 to n-1:
        // Invariant: ...
        ...
    // Postcondition: ...
    return x
```

---

## Pseudocode → C / C++ / Python

| Pseudocode | C | C++ | Python |
|---|---|---|---|
| `for i = 0 to n-1` | `for(int i=0;i<n;i++)` | `for(int i=0;i<n;i++)` | `for i in range(n):` |
| `for i = 1 to n` | `for(int i=1;i<=n;i++)` | `for(int i=1;i<=n;i++)` | `for i in range(1, n+1):` |
| `for i = n-1 down to 0` | `for(int i=n-1;i>=0;i--)` | `for(int i=n-1;i>=0;i--)` | `for i in range(n-1,-1,-1):` |
| `else if` | `else if` | `else if` | `elif` |
| `a div b` | `a / b` | `a / b` | `a // b` |
| `a mod b` | `a % b` | `a % b` | `a % b` |
| `swap(a, b)` | `t=a; a=b; b=t;` | `swap(a,b);` | `a, b = b, a` |
| `repeat ... until c` | `do{...}while(!c);` | `do{...}while(!c);` | `while True: ...; if c: break` |
| `array of size n filled with 0` | `int a[N]={0};` | `vector<int> a(n,0);` | `a=[0]*n` |
| `B = array n × m` | `int b[N][M];` | `vector<vector<int>> b(n,vector<int>(m));` | `b=[[0]*m for _ in range(n)]` |
| `length(A)` | `n` (alohida) | `a.size()` | `len(a)` |
| `append(A, x)` | — | `a.push_back(x);` | `a.append(x)` |
| `INF` | `INT_MAX` / `1e18` | `INT_MAX` / `LLONG_MAX` | `float('inf')` |
| `NIL` | `NULL` / `-1` | `nullptr` / `-1` | `None` |
| `read n` | `scanf("%d",&n);` | `cin >> n;` | `n=int(input())` |
| `print x` | `printf("%d\n",x);` | `cout << x << "\n";` | `print(x)` |

---

## Tarjimadagi 8 tuzoq

| # | Tuzoq | Choralar |
|---|---|---|
| 1 | Off-by-one (`to` kiradi, `range` kirmaydi) | Yuqoridagi jadval |
| 2 | Overflow (C/C++ `int` ~ $2 \cdot 10^9$) | `long long`, pseudocode'da `// 64-bit` |
| 3 | Manfiy `div` / `mod` (C++ nolga, Python pastga yaxlitlaydi) | Manfiy bo'lsa alohida izohlang |
| 4 | Python `/` real qaytaradi | Butun uchun `//` |
| 5 | `[[0]*m]*n` (qatorlar bitta ob'ekt) | `[[0]*m for _ in range(n)]` |
| 6 | C da lokal massiv chiqindi qiymat | `= {0}` yoki `memset` |
| 7 | Python `pop(0)`, `x in list` — $O(n)$ | `deque`, `set` |
| 8 | Python rekursiya chegarasi ~1000 | `setrecursionlimit` yoki iterativ |

---

## Chek-list (kodga o'tishdan oldin)

- [ ] Sarlavha to'liqmi (INPUT/OUTPUT/TIME/SPACE)?
- [ ] Indeks/oraliq konventsiyasi aniqmi?
- [ ] Hamma o'zgaruvchi inisializatsiya qilinganmi?
- [ ] Har siklda invariant va tugash sharti bormi?
- [ ] Rekursiyada base case bormi, masala kichrayyaptimi?
- [ ] Kamida bitta misolda **trace** qilinganmi?
- [ ] Edge case'lar: `n=0`, `n=1`, hammasi teng, maksimal $n$?
- [ ] Complexity cheklovga sig'adimi? Overflow xavfi bormi?
