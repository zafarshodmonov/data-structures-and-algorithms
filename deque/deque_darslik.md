# Deque (Double-Ended Queue) — To'liq Darslik

## Mundarija
1. [Deque nima?](#1-deque-nima)
2. [Deque qachon kerak bo'ladi?](#2-deque-qachon-kerak-boladi)
3. [Ichki tuzilishi (qanday ishlaydi)](#3-ichki-tuzilishi)
4. [Python: `collections.deque`](#4-python-collectionsdeque)
5. [C++: `std::deque`](#5-c-stddeque)
6. [C tilida deque (built-in yo'q, o'zimiz yasaymiz)](#6-c-tilida-deque)
7. [Murakkablik (Time Complexity) solishtiruvi](#7-murakkablik-solishtiruvi)
8. [Amaliy masalalar (Competitive Programming)](#8-amaliy-masalalar)
9. [Umumiy xatolar va maslahatlar](#9-umumiy-xatolar-va-maslahatlar)
10. [Xulosa jadvali](#10-xulosa-jadvali)

---

## 1. Deque nima?

**Deque** — *Double-Ended Queue* (ikki tomonlama navbat) so'zining qisqartmasi. Bu — ham boshidan (front), ham oxiridan (back/rear) elementlarni **O(1)** vaqtda qo'shish va olib tashlash imkonini beruvchi ma'lumotlar tuzilmasi.

Oddiy tushuncha uchun taqqoslaymiz:

| Tuzilma | Qo'shish/olish joyi |
|---|---|
| **Stack** (steк) | Faqat bitta uchidan (LIFO — oxirgi kirgan birinchi chiqadi) |
| **Queue** (navbat) | Bir uchidan qo'shiladi, boshqa uchidan olinadi (FIFO) |
| **Deque** | **Ikkala uchidan** ham qo'shish/olish mumkin |

Deque — Stack va Queue'ning "kengaytirilgan" versiyasi deb tasavvur qiling: u ikkalasining vazifasini ham bajara oladi.

```
    front                          back
      |                             |
      v                             v
  [ 10 ][ 20 ][ 30 ][ 40 ][ 50 ]
      ^                             ^
   bu yerdan ham              bu yerdan ham
   qo'shish/olish              qo'shish/olish
   mumkin (O(1))               mumkin (O(1))
```

---

## 2. Deque qachon kerak bo'ladi?

Deque quyidagi holatlarda **eng to'g'ri tanlov**:

1. **BFS (Breadth-First Search)** — navbat sifatida ishlatiladi (`popleft`, `append`).
2. **0-1 BFS** — og'irligi 0 yoki 1 bo'lgan grafda: 0 og'irlikda `appendleft`, 1 og'irlikda `append`.
3. **Sliding Window (siljiydigan oyna) masalalari** — masalan, oynadagi maksimum/minimumni topish (Monotonic Deque).
4. **Palindrome tekshirish** — ikkala uchidan bir vaqtda solishtirish.
5. **Undo/Redo tizimlari**, **brauzer tarixi** (oldinga/orqaga).
6. **Cache implementatsiyasi** (masalan LRU Cache'ning yordamchi qismi sifatida).
7. Massivning **ikkala boshiga** ham tez-tez element qo'shish/olish kerak bo'lganda (oddiy array yoki Python list bunda sekin, chunki boshidan olish/qo'shish **O(n)**).

**Muhim qoida:** Agar sizga faqat oxiridan ishlash kerak bo'lsa — oddiy `list`/`vector`/`array` yetarli. Agar **boshidan ham** tez-tez ishlov berish kerak bo'lsa — **deque tanlang**.

---

## 3. Ichki tuzilishi

Deque odatda ikki xil usulda amalga oshiriladi:

### a) Dinamik massivlar bloklari (Python va C++ standart implementatsiyasi)
Deque bitta uzluksiz massiv emas — u **kichik bloklar (chunk)** ketma-ketligidan iborat. Har bir blok belgilangan hajmga ega, va bloklarga ko'rsatkichlar (pointer) massivi orqali murojaat qilinadi.

```
Block pointer array:  [ptr1] [ptr2] [ptr3] ...
                         |      |      |
                         v      v      v
                      [block1][block2][block3]
```

Bu tufayli:
- Boshiga yoki oxiriga qo'shish — yangi blok kerak bo'lmasa **O(1)**.
- O'rtadan element olish (`d[i]`) — **O(1)** ga yaqin, lekin oddiy massivdan sal sekinroq (indeksni hisoblash kerak).
- **Vector**dan farqli o'laroq, deque'ga boshidan qo'shish uchun butun massivni ko'chirish shart emas.

### b) Doiraviy bufer (Circular Buffer)
Ba'zi implementatsiyalarda (masalan, o'zimiz C'da yozganimizda) deque **doiraviy massiv** yordamida ham qilinadi — `front` va `back` indekslari massiv chegarasidan chiqsa, boshiga qaytadi (modulo orqali).

### c) Ikki tomonlama bog'langan ro'yxat (Doubly Linked List)
Har bir tugun oldingi va keyingi tugunga ko'rsatkichga ega. Bunda hech qanday ko'chirish kerak emas, lekin xotira sarfi ko'proq (har bir element uchun 2 ta pointer) va cache-locality yomonroq.

---

## 4. Python: `collections.deque`

### 4.1 Import va yaratish

```python
from collections import deque

d1 = deque()                      # bo'sh deque
d2 = deque([1, 2, 3, 4])          # ro'yxatdan yaratish
d3 = deque([1, 2, 3], maxlen=5)   # maksimal uzunlik bilan
```

`maxlen` parametri juda foydali: deque to'lib ketsa, eng "eski" element avtomatik chiqarib tashlanadi (bu — **circular buffer / sliding window** uchun ideal).

```python
d = deque(maxlen=3)
d.append(1); d.append(2); d.append(3)
d.append(4)
print(d)   # deque([2, 3, 4], maxlen=3)  -> 1 avtomatik chiqib ketdi
```

### 4.2 Barcha metodlar to'liq ro'yxati

| Metod | Vazifasi | Murakkablik |
|---|---|---|
| `append(x)` | Oxiriga `x` qo'shadi | O(1) |
| `appendleft(x)` | Boshiga `x` qo'shadi | O(1) |
| `pop()` | Oxiridan elementni olib, qaytaradi | O(1) |
| `popleft()` | Boshidan elementni olib, qaytaradi | O(1) |
| `extend(iterable)` | Oxiriga bir nechta elementni qo'shadi | O(k) |
| `extendleft(iterable)` | Boshiga qo'shadi (**tartib teskari bo'ladi!**) | O(k) |
| `insert(i, x)` | `i`-indeksga `x` ni joylaydi | O(n) |
| `remove(x)` | Birinchi uchragan `x` ni o'chiradi | O(n) |
| `count(x)` | `x` necha marta uchraganini sanaydi | O(n) |
| `index(x[, start[, stop]])` | `x` ning indeksini topadi | O(n) |
| `rotate(n)` | Elementlarni `n` pozitsiyaga suradi (o'ngga, manfiy bo'lsa chapga) | O(k) |
| `reverse()` | Deque'ni teskari tartibga o'zgartiradi (in-place) | O(n) |
| `clear()` | Barcha elementlarni o'chiradi | O(n) |
| `copy()` | Sayoz nusxa (shallow copy) yaratadi | O(n) |
| `len(d)` | Uzunligini qaytaradi | O(1) |
| `d[i]` | `i`-indeksdagi elementga murojaat | O(n) chetlarga yaqin bo'lsa tezroq |
| `maxlen` (property) | Maksimal uzunlikni ko'rsatadi (faqat o'qish) | O(1) |

### 4.3 Har bir metod uchun misollar

```python
from collections import deque

d = deque([1, 2, 3])

d.append(4)          # deque([1, 2, 3, 4])
d.appendleft(0)       # deque([0, 1, 2, 3, 4])

d.pop()               # 4 ni qaytaradi -> deque([0, 1, 2, 3])
d.popleft()           # 0 ni qaytaradi -> deque([1, 2, 3])

d.extend([4, 5])          # deque([1, 2, 3, 4, 5])
d.extendleft([0, -1])     # deque([-1, 0, 1, 2, 3, 4, 5])
# DIQQAT: extendleft har bir elementni birma-bir boshiga qo'shadi,
# shuning uchun natijada tartib teskari bo'ladi!

d.rotate(1)     # oxirgi elementni boshiga suradi: [5, -1, 0, 1, 2, 3, 4]
d.rotate(-2)    # boshidagi 2 ta elementni oxiriga suradi

d.reverse()     # butun deque'ni teskari qiladi

print(d.count(3))     # nechta 3 bor - sanaydi
print(d.index(2))     # 2 ning indeksi

d.remove(2)     # birinchi topilgan 2 ni o'chiradi
d.insert(1, 99) # 1-indeksga 99 qo'yadi

d2 = d.copy()   # nusxa

d.clear()       # bo'shatadi
```

### 4.4 `rotate()` ni chuqurroq tushunish

```python
d = deque([1, 2, 3, 4, 5])
d.rotate(2)     # o'ngga 2 ta surish
print(d)        # deque([4, 5, 1, 2, 3])

d.rotate(-2)    # chapga 2 ta surish (asl holatga qaytadi)
print(d)        # deque([1, 2, 3, 4, 5])
```

`rotate(n)` — aylana buferni aylantirishga o'xshaydi: musiqa albomidagi treklarni aylanma tartibda siljitish kabi.

### 4.5 Python'da amaliy foydalanish — BFS misoli

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    q = deque([start])
    order = []
    while q:
        node = q.popleft()      # navbat boshidan olamiz -> O(1)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)   # oxiriga qo'shamiz -> O(1)
    return order

graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
print(bfs(graph, 1))   # [1, 2, 3, 4]
```

**Nega `list` emas, `deque`?** Agar `list.pop(0)` ishlatilsa, bu **O(n)** — chunki Python listda boshidagi elementni olib tashlagach, qolgan barcha elementlar bir pozitsiyaga siljitiladi. Katta grafada bu juda sekin bo'lib qoladi. `deque.popleft()` esa doim **O(1)**.

### 4.6 Sliding Window Maximum (Monotonic Deque) — AtCoder uslubidagi masala

```python
from collections import deque

def sliding_window_max(nums, k):
    dq = deque()   # bu yerda indekslarni saqlaymiz
    result = []
    for i, num in enumerate(nums):
        # oynadan chiqib ketgan indekslarni olib tashlaymiz
        while dq and dq[0] <= i - k:
            dq.popleft()
        # o'zidan kichik elementlarni deque oxiridan chiqarib tashlaymiz
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))
# [3, 3, 5, 5, 6, 7]
```

Bu — deque'ning eng klassik va kuchli qo'llanilishlaridan biri: **O(n)** vaqtda har bir oynadagi maksimumni topish.

---

## 5. C++: `std::deque`

`std::deque` — `<deque>` sarlavha faylida joylashgan, STL konteyner.

### 5.1 E'lon qilish

```cpp
#include <deque>
#include <iostream>
using namespace std;

deque<int> d;                  // bo'sh deque
deque<int> d2 = {1, 2, 3, 4};  // initializer list bilan
deque<int> d3(5, 10);          // 5 ta 10 dan iborat: {10,10,10,10,10}
```

### 5.2 Barcha metodlar to'liq ro'yxati

**Elementga kirish (Element Access):**

| Metod | Vazifasi |
|---|---|
| `d.at(i)` | `i`-indeksdagi elementga xavfsiz (chegaradan chiqsa `out_of_range` istisno) kirish |
| `d[i]` | Indeks orqali kirish (chegara tekshirilmaydi) |
| `d.front()` | Birinchi elementni qaytaradi |
| `d.back()` | Oxirgi elementni qaytaradi |

**Iteratorlar:**

| Metod | Vazifasi |
|---|---|
| `d.begin()` / `d.end()` | Boshi va oxiridan keyingi iterator |
| `d.rbegin()` / `d.rend()` | Teskari iteratorlar |
| `d.cbegin()` / `d.cend()` | Const iteratorlar |

**Hajm (Capacity):**

| Metod | Vazifasi |
|---|---|
| `d.empty()` | Bo'shligini tekshiradi (`bool`) |
| `d.size()` | Elementlar sonini qaytaradi |
| `d.max_size()` | Nazariy maksimal hajm |
| `d.shrink_to_fit()` | Ortiqcha xotirani qaytarishga urinadi |

**O'zgartirish (Modifiers):**

| Metod | Vazifasi | Murakkablik |
|---|---|---|
| `d.push_back(x)` | Oxiriga qo'shadi | O(1) |
| `d.push_front(x)` | Boshiga qo'shadi | O(1) |
| `d.pop_back()` | Oxirgi elementni o'chiradi | O(1) |
| `d.pop_front()` | Birinchi elementni o'chiradi | O(1) |
| `d.emplace_back(args...)` | Oxirida to'g'ridan-to'g'ri obyekt yaratadi (nusxalashsiz) | O(1) amortiz. |
| `d.emplace_front(args...)` | Boshida to'g'ridan-to'g'ri obyekt yaratadi | O(1) amortiz. |
| `d.emplace(it, args...)` | Ko'rsatilgan joyda obyekt yaratadi | O(n) |
| `d.insert(it, x)` | Iterator ko'rsatgan joyga qo'shadi | O(n) |
| `d.erase(it)` | Ko'rsatilgan joydagi elementni o'chiradi | O(n) |
| `d.clear()` | Barchasini tozalaydi | O(n) |
| `d.resize(n)` | Hajmini o'zgartiradi | O(n) |
| `d.swap(other)` | Ikkita deque'ni almashtiradi | O(1) |
| `d.assign(n, val)` | `n` ta `val` bilan to'ldiradi | O(n) |

### 5.3 Misollar

```cpp
#include <deque>
#include <iostream>
using namespace std;

int main() {
    deque<int> d = {1, 2, 3};

    d.push_back(4);       // {1,2,3,4}
    d.push_front(0);      // {0,1,2,3,4}

    cout << d.front() << " " << d.back() << endl;   // 0 4

    d.pop_back();          // {0,1,2,3}
    d.pop_front();         // {1,2,3}

    d.emplace_back(10);    // {1,2,3,10} - to'g'ridan-to'g'ri qurish
    d.emplace_front(-1);   // {-1,1,2,3,10}

    for (int x : d) cout << x << " ";  // -1 1 2 3 10
    cout << endl;

    cout << d.at(2) << endl;   // 2 (xavfsiz kirish)
    d[0] = 100;                 // {100,1,2,3,10}

    d.insert(d.begin() + 2, 999);  // 2-indeksga 999 qo'yadi
    d.erase(d.begin());            // birinchi elementni o'chiradi

    cout << d.size() << endl;
    d.clear();
    cout << boolalpha << d.empty() << endl;  // true
}
```

### 5.4 `std::deque` vs `std::vector`

| Xususiyat | `vector` | `deque` |
|---|---|---|
| Xotirada joylashuvi | Uzluksiz (contiguous) | Bloklar ketma-ketligi |
| `push_back` | O(1) amortiz. | O(1) amortiz. |
| `push_front` | **O(n)** (barchasini ko'chirish kerak) | **O(1)** |
| Random access `[i]` | Juda tez (cache-friendly) | Tez, lekin `vector`dan sal sekinroq |
| Pointer/iterator barqarorligi | `push_back` da bekor bo'lishi mumkin | Chetdagi qo'shishlarda ko'proq barqaror |

**Xulosa:** Agar sizga faqat orqasiga qo'shish kerak bo'lsa — `vector` ishlating (u tezroq va xotira jihatidan tejamli). Agar boshiga ham tez-tez qo'shish/olish kerak bo'lsa — `deque`.

### 5.5 C++'da `deque` orqali stack/queue

STL'da `stack` va `queue` konteynerlari ichki tomondan **standart bo'yicha `deque`dan foydalanadi** (bu — "container adapter" deb ataladi):

```cpp
#include <stack>
#include <queue>

stack<int> s;   // ichida deque<int> ishlatiladi
queue<int> q;   // ichida deque<int> ishlatiladi
```

---

## 6. C tilida deque

C tilida **built-in deque yo'q** (standart kutubxonada). Shuning uchun uni odatda ikki usulda o'zimiz yasaymiz:

### 6.1 Usul A — Doiraviy massiv (Circular Array) orqali

Bu — sobit hajmli, lekin juda tez ishlaydigan variant.

```c
#include <stdio.h>
#include <stdbool.h>

#define CAPACITY 100

typedef struct {
    int data[CAPACITY];
    int front;   // birinchi elementning indeksi
    int back;    // keyingi bo'sh joy indeksi (oxiridan keyin)
    int count;   // hozirgi elementlar soni
} Deque;

void deque_init(Deque *dq) {
    dq->front = 0;
    dq->back = 0;
    dq->count = 0;
}

bool deque_is_empty(Deque *dq) {
    return dq->count == 0;
}

bool deque_is_full(Deque *dq) {
    return dq->count == CAPACITY;
}

// Oxiriga qo'shish - push_back
bool deque_push_back(Deque *dq, int value) {
    if (deque_is_full(dq)) return false;
    dq->data[dq->back] = value;
    dq->back = (dq->back + 1) % CAPACITY;   // doiraviy siljish
    dq->count++;
    return true;
}

// Boshiga qo'shish - push_front
bool deque_push_front(Deque *dq, int value) {
    if (deque_is_full(dq)) return false;
    dq->front = (dq->front - 1 + CAPACITY) % CAPACITY;
    dq->data[dq->front] = value;
    dq->count++;
    return true;
}

// Oxiridan olish - pop_back
bool deque_pop_back(Deque *dq, int *out) {
    if (deque_is_empty(dq)) return false;
    dq->back = (dq->back - 1 + CAPACITY) % CAPACITY;
    *out = dq->data[dq->back];
    dq->count--;
    return true;
}

// Boshidan olish - pop_front
bool deque_pop_front(Deque *dq, int *out) {
    if (deque_is_empty(dq)) return false;
    *out = dq->data[dq->front];
    dq->front = (dq->front + 1) % CAPACITY;
    dq->count--;
    return true;
}

int deque_front(Deque *dq) { return dq->data[dq->front]; }
int deque_back(Deque *dq)  { return dq->data[(dq->back - 1 + CAPACITY) % CAPACITY]; }

int main() {
    Deque dq;
    deque_init(&dq);

    deque_push_back(&dq, 10);
    deque_push_back(&dq, 20);
    deque_push_front(&dq, 5);

    printf("front: %d, back: %d\n", deque_front(&dq), deque_back(&dq));
    // front: 5, back: 20

    int val;
    deque_pop_front(&dq, &val);
    printf("olingan: %d\n", val);   // 5

    return 0;
}
```

**Muhim tushuntirish:** `(x + 1) % CAPACITY` va `(x - 1 + CAPACITY) % CAPACITY` — bu **doiraviy indeks hisoblash** formulasi. Massiv chegarasidan chiqib ketsa, boshiga (yoki oxiriga) "aylanib" qaytadi — xuddi soat mili kabi.

### 6.2 Usul B — Ikki tomonlama bog'langan ro'yxat (Doubly Linked List) orqali

Bu usul — hajmi oldindan noma'lum bo'lganda foydalidir (dinamik o'sadi).

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *prev;
    struct Node *next;
} Node;

typedef struct {
    Node *front;
    Node *back;
    int size;
} Deque;

void deque_init(Deque *dq) {
    dq->front = NULL;
    dq->back = NULL;
    dq->size = 0;
}

void deque_push_back(Deque *dq, int value) {
    Node *node = (Node*)malloc(sizeof(Node));
    node->data = value;
    node->next = NULL;
    node->prev = dq->back;

    if (dq->back) dq->back->next = node;
    else dq->front = node;   // deque bo'sh edi

    dq->back = node;
    dq->size++;
}

void deque_push_front(Deque *dq, int value) {
    Node *node = (Node*)malloc(sizeof(Node));
    node->data = value;
    node->prev = NULL;
    node->next = dq->front;

    if (dq->front) dq->front->prev = node;
    else dq->back = node;

    dq->front = node;
    dq->size++;
}

int deque_pop_front(Deque *dq) {
    if (!dq->front) { printf("Deque bo'sh!\n"); exit(1); }
    Node *old = dq->front;
    int value = old->data;

    dq->front = old->next;
    if (dq->front) dq->front->prev = NULL;
    else dq->back = NULL;

    free(old);
    dq->size--;
    return value;
}

int deque_pop_back(Deque *dq) {
    if (!dq->back) { printf("Deque bo'sh!\n"); exit(1); }
    Node *old = dq->back;
    int value = old->data;

    dq->back = old->prev;
    if (dq->back) dq->back->next = NULL;
    else dq->front = NULL;

    free(old);
    dq->size--;
    return value;
}

void deque_free(Deque *dq) {
    while (dq->size > 0) deque_pop_front(dq);
}

int main() {
    Deque dq;
    deque_init(&dq);

    deque_push_back(&dq, 1);
    deque_push_back(&dq, 2);
    deque_push_front(&dq, 0);

    printf("%d\n", deque_pop_front(&dq));  // 0
    printf("%d\n", deque_pop_back(&dq));   // 2
    printf("%d\n", deque_pop_front(&dq));  // 1

    deque_free(&dq);
    return 0;
}
```

**Ikki usulni solishtirish:**

| | Doiraviy massiv | Bog'langan ro'yxat |
|---|---|---|
| Xotira | Tejamli, cache-friendly | Har bir tugun uchun qo'shimcha 2 pointer |
| Hajm | Sobit (yoki qayta o'lchash kerak) | Dinamik, cheklovsiz |
| Tezlik | Juda tez (massivga bevosita murojaat) | Sal sekinroq (pointer'larga ergashish) |
| Amalga oshirish qiyinligi | O'rtacha | Sal murakkabroq (4 ta holatni: bo'sh, bitta element va h.k. hisobga olish kerak) |

---

## 7. Murakkablik solishtiruvi

| Amal | Python `deque` | C++ `std::deque` | C (qo'lda, massiv) | C (qo'lda, linked list) |
|---|---|---|---|---|
| `push_back` / `append` | O(1) | O(1) amortiz. | O(1) | O(1) |
| `push_front` / `appendleft` | O(1) | O(1) amortiz. | O(1) | O(1) |
| `pop_back` / `pop` | O(1) | O(1) | O(1) | O(1) |
| `pop_front` / `popleft` | O(1) | O(1) | O(1) | O(1) |
| Indeks orqali kirish `d[i]` | O(n) (chetlarga yaqin bo'lsa tezroq) | O(1) ga yaqin | O(1) | O(n) |
| O'rtadan qo'shish/o'chirish | O(n) | O(n) | O(n) | O(n) |
| `rotate` / aylantirish | O(k) | Yo'q (qo'lda qilinadi) | Qo'lda | Qo'lda |

**Diqqat:** Python'dagi `deque[i]` C++'dagi `deque[i]`dan sekinroq, chunki Python implementatsiyasi bloklar bo'ylab yurishi kerak. Shuning uchun Python'da deque'ni **ko'p marta indekslash** kerak bo'lsa (masalan tasodifiy kirish ko'p bo'lsa), `list` ko'proq mos kelishi mumkin — lekin boshi/oxiridan qo'shish/olish bo'lsa, `deque` doim yutadi.

---

## 8. Amaliy masalalar

### 8.1 Palindrome tekshirish (Python)

```python
from collections import deque

def is_palindrome(s):
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print(is_palindrome("abcba"))   # True
print(is_palindrome("abccba"))  # True
print(is_palindrome("abcde"))   # False
```

### 8.2 0-1 BFS (C++ uslubida, lekin tushuntirish umumiy)

Grafda qirralar og'irligi faqat 0 yoki 1 bo'lsa, oddiy Dijkstra o'rniga **deque asosidagi BFS** ishlatiladi:

```
Agar qirra og'irligi 0 bo'lsa -> deque OLDIGA qo'shiladi (push_front)
Agar qirra og'irligi 1 bo'lsa -> deque OXIRIGA qo'shiladi (push_back)
```

Bu — deque'ning eng "aqlli" ishlatilishlaridan biri, chunki u deque'ni har doim **saralangan holatda** ushlab turadi (0-og'irlikdagi tugunlar doim navbat boshida bo'ladi), va Dijkstra'ning O(E log V) o'rniga **O(V + E)** vaqt beradi.

### 8.3 C++ kod: Deque bilan Sliding Window Maximum

```cpp
#include <deque>
#include <vector>
#include <iostream>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;   // indekslarni saqlaydi
    vector<int> result;

    for (int i = 0; i < (int)nums.size(); i++) {
        while (!dq.empty() && dq.front() <= i - k)
            dq.pop_front();

        while (!dq.empty() && nums[dq.back()] < nums[i])
            dq.pop_back();

        dq.push_back(i);

        if (i >= k - 1)
            result.push_back(nums[dq.front()]);
    }
    return result;
}

int main() {
    vector<int> nums = {1,3,-1,-3,5,3,6,7};
    vector<int> res = maxSlidingWindow(nums, 3);
    for (int x : res) cout << x << " ";
    // 3 3 5 5 6 7
}
```

Bu — LeetCode'ning mashhur "Sliding Window Maximum" masalasi, va deque bu yerda **O(n)** yechimga imkon beradi (naive yechim bo'lsa O(n·k) bo'lardi).

---

## 9. Umumiy xatolar va maslahatlar

1. **Python'da `list.pop(0)` ishlatmang** — bu O(n). Buning o'rniga `deque.popleft()` dan foydalaning.
2. **`extendleft()` tartibni teskari qiladi** — agar `[1,2,3]` ni `extendleft` qilsangiz, natija `[3,2,1,...]` bo'ladi, chunki har bir element birma-bir boshiga qo'yiladi.
3. **C++'da `deque`ning o'rtasiga `insert`/`erase` qilinganda iteratorlar bekor bo'ladi** — bu haqda ehtiyot bo'ling, `vector`dagi kabi.
4. **C'da doiraviy massiv usulida `CAPACITY` chegarasidan chiqib ketishni albatta tekshiring** — `is_full()` funksiyasini har doim chaqiring.
5. **Deque'ni tasodifiy (random) indekslash ko'p bo'ladigan joyda ishlatmang** — u uchun `vector`/`list` ko'proq mos.
6. **AtCoder/competitive programming'da**: agar masalada "navbatning ham boshidan, ham oxiridan ishlov berish" kerak bo'lsa (masalan sliding window, 0-1 BFS, ba'zi greedy masalalar) — bu deque kerakligining aniq belgisi.

---

## 10. Xulosa jadvali

| Til | Qanday chaqiriladi | Qo'shish (old/orqa) | Olish (old/orqa) | Xususiyati |
|---|---|---|---|---|
| **Python** | `from collections import deque` | `appendleft` / `append` | `popleft` / `pop` | `maxlen` bilan avtomatik cheklash, `rotate()` mavjud |
| **C++** | `#include <deque>` | `push_front` / `push_back` | `pop_front` / `pop_back` | STL konteyner, `stack`/`queue` uning ustiga qurilgan |
| **C** | Built-in yo'q, o'zingiz yozasiz | Qo'lda: doiraviy massiv yoki linked list | Qo'lda | To'liq nazorat, lekin ko'proq kod yozish kerak |

**Umumiy qoida:** Har uchala tilda ham deque'ning mag'zi bir xil — u sizga **ikkala uchidan ham O(1) vaqtda ishlash** imkonini beradi. Farq faqat **sintaksis** va **ichki implementatsiya detallarida**.

---

*Agar biror qismini chuqurroq tushuntirishimni yoki qo'shimcha mashqlar (masalan AtCoder uslubidagi masalalar) tayyorlashimni istasangiz, ayting.*
