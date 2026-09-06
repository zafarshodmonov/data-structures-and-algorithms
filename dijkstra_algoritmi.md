# Dijkstra Algoritmi — To'liq Darslik

## 1. Kirish: Muammo nima?

Tasavvur qiling, sizda shaharlar orasidagi yo'llar tarmog'i bor, va har bir yo'lning uzunligi (yoki narxi, vaqt) ma'lum. Sizga bitta shahardan (masalan, Toshkentdan) boshlab, qolgan **barcha** shaharlargacha bo'lgan **eng qisqa masofani** topish kerak.

Bu **Single-Source Shortest Path (SSSP)** muammosi deb ataladi — bitta manba (source) tugundan grafdagi barcha boshqa tugunlargacha eng qisqa yo'lni topish.

**Dijkstra algoritmi** (Edsger W. Dijkstra tomonidan 1956-yilda ixtiro qilingan) — bu muammoni **manfiy bo'lmagan og'irliklarga (non-negative weights)** ega graflarda samarali hal qiluvchi eng mashhur algoritm.

### Qayerda ishlatiladi?
- GPS navigatsiya tizimlari (Google Maps)
- Tarmoq routing protokollari (OSPF)
- O'yinlarda pathfinding
- Ijtimoiy tarmoq tahlili

## 2. Asosiy g'oya (Intuition)

Dijkstra algoritmining markazidagi g'oya — **greedy (ochko'z) yondashuv**:

> Har doim, hozircha topilgan eng qisqa masofaga ega, hali "yakunlanmagan" tugunni tanlab, undan chiqadigan qirralar orqali qo'shni tugunlarning masofasini yangilaymiz (relaxation).

Buni shunday tasavvur qilish mumkin: siz manba nuqtadan boshlab, "to'lqin" tarqatasiz. Har safar eng yaqin tugunga yetib borgach, u orqali qolgan tugunlarga yetib borish yo'lini tekshirib ko'rasiz — agar yangi yo'l qisqaroq bo'lsa, uni yangilaymiz.

**Muhim shart:** Qirralarning og'irligi **manfiy bo'lmasligi** kerak. Aks holda algoritm noto'g'ri natija berishi mumkin (buning sababini pastda ko'ramiz).

## 3. Algoritm qanday ishlaydi — qadam-baqadam

### Kerakli ma'lumotlar:
- `dist[]` — massiv, har bir tugungacha hozirda ma'lum bo'lgan eng qisqa masofa (boshida `dist[source] = 0`, qolganlari `infinity`)
- `visited[]` — tugun "yakunlangan" (finalized) yoki yo'qligini bildiradi
- Priority queue (min-heap) — eng kichik `dist` qiymatiga ega tugunni tez topish uchun

### Qadamlar:
1. `dist[source] = 0`, qolgan barcha tugunlar uchun `dist[v] = infinity`
2. Priority queue'ga `(0, source)` qo'shiladi
3. Priority queue bo'sh bo'lmaguncha:
   - Navbatdan eng kichik `dist` qiymatiga ega tugun `u` olinadi
   - Agar `u` allaqachon `visited` bo'lsa — o'tkazib yuboriladi (eskirgan yozuv)
   - `u` ni `visited = true` deb belgilanadi
   - `u`ning har bir qo'shnisi `v` uchun: agar `dist[u] + weight(u, v) < dist[v]` bo'lsa, `dist[v]` yangilanadi va `(dist[v], v)` navbatga qo'shiladi (bu — **relaxation** operatsiyasi)
4. Barcha tugunlar `visited` bo'lganda, `dist[]` massivi — manbadan har bir tugungacha bo'lgan eng qisqa masofalar

### Konkret misol

Quyidagi graf berilgan (tugunlar: A, B, C, D, E; A — manba):

```
A --4--> B
A --1--> C
C --2--> B
C --5--> D
B --1--> D
D --3--> E
```

**Boshlanish:** `dist = {A:0, B:∞, C:∞, D:∞, E:∞}`

| Qadam | Tanlangan tugun | Yangilanishlar | dist holati |
|---|---|---|---|
| 1 | A (0) | B=4, C=1 | A:0, B:4, C:1, D:∞, E:∞ |
| 2 | C (1) | B=min(4,1+2)=3, D=1+5=6 | A:0, B:3, C:1, D:6, E:∞ |
| 3 | B (3) | D=min(6,3+1)=4 | A:0, B:3, C:1, D:4, E:∞ |
| 4 | D (4) | E=4+3=7 | A:0, B:3, C:1, D:4, E:7 |
| 5 | E (7) | — | A:0, B:3, C:1, D:4, E:7 |

**Natija:** A dan har bir tugungacha eng qisqa masofa: B=3 (A→C→B), C=1 (A→C), D=4 (A→C→B→D), E=7.

Bu yerda muhim narsa: B ga to'g'ridan-to'g'ri borish (4) emas, C orqali borish (1+2=3) qisqaroq ekanligi aniqlandi — bu **relaxation**ning mohiyati.

## 4. Pseudocode

```
function Dijkstra(Graph, source):
    dist = array of size |V|, filled with infinity
    dist[source] = 0
    visited = array of size |V|, filled with false
    PQ = min-priority-queue()
    PQ.insert(0, source)

    while PQ is not empty:
        (d, u) = PQ.extract_min()
        if visited[u]:
            continue
        visited[u] = true

        for each neighbor v of u with edge weight w:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                PQ.insert(dist[v], v)

    return dist
```

## 5. Nega ishlaydi? (To'g'riligi isboti — intuitiv)

Dijkstra algoritmining to'g'riligi quyidagi kuzatuvga asoslanadi:

**Da'vo:** Har safar priority queue'dan eng kichik `dist` qiymatiga ega tugun `u` chiqarilganda, `dist[u]` qiymati **allaqachon yakuniy va to'g'ri** bo'ladi.

**Nega?** Chunki barcha qirralar manfiy bo'lmagan og'irlikka ega. Agar `u`gacha boshqa, hali tekshirilmagan yo'l orqali qisqaroq masofa mavjud bo'lsa, u yo'l albatta hali navbatda turgan (visited bo'lmagan) boshqa bir tugun `x` orqali o'tishi kerak edi, va `dist[x] <= dist[u]` bo'lardi (chunki og'irliklar manfiy emas, yo'l davomida masofa faqat oshib boradi). Ammo biz `u`ni tanladik, chunki u navbatda **eng kichik** `dist` qiymatiga ega edi — demak bunday `x` mavjud bo'lolmaydi. Ziddiyat.

**Nega manfiy og'irliklarda ishlamaydi?** Agar qirralar manfiy bo'lsa, "keyinroq" topilgan yo'l orqali masofani **kamaytirish** mumkin bo'ladi — ya'ni yakunlangan (visited) tugunning `dist` qiymati keyinchalik yanada kamayishi kerak bo'lib qolishi mumkin, lekin algoritm bu tugunni qayta ko'rib chiqmaydi. Bunday holatda **Bellman-Ford algoritmi** ishlatiladi.

## 6. Murakkablik tahlili (Complexity Analysis)

Dijkstra algoritmining murakkabligi qanday ma'lumotlar tuzilmasi ishlatilishiga bog'liq:

| Implementatsiya | Vaqt murakkabligi | Izoh |
|---|---|---|
| Adjacency matrix + oddiy massiv (min qidirish) | O(V²) | Kichik/zich (dense) graflar uchun yaxshi |
| Adjacency list + binary heap (priority_queue) | O((V + E) log V) | Ko'pchilik holatlar uchun standart tanlov |
| Adjacency list + Fibonacci heap | O(E + V log V) | Nazariy jihatdan eng tez, amalda kamdan-kam ishlatiladi |

**Xotira murakkabligi:** O(V + E) — grafni saqlash uchun (adjacency list holatida).

Qaerda:
- **V** — tugunlar (vertices) soni
- **E** — qirralar (edges) soni

Bizning implementatsiyalarimizda biz **binary heap (priority_queue / heapq)** yondashuvidan foydalanamiz, chunki u amaliyotda eng ko'p qo'llaniladi va sodda.

## 7. Implementatsiyalar

### 7.1 C++ (priority_queue bilan)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

vector<long long> dijkstra(int n, int source, vector<vector<pair<int,int>>>& adj) {
    // adj[u] = list of (neighbor, weight)
    vector<long long> dist(n, INF);
    dist[source] = 0;

    // min-heap: (distance, node)
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
    pq.push({0, source});

    vector<bool> visited(n, false);

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (visited[u]) continue; // eskirgan yozuv, o'tkazib yuboramiz
        visited[u] = true;

        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

int main() {
    int n = 5; // A=0, B=1, C=2, D=3, E=4
    vector<vector<pair<int,int>>> adj(n);

    auto addEdge = [&](int u, int v, int w) {
        adj[u].push_back({v, w});
    };

    addEdge(0, 1, 4); // A->B
    addEdge(0, 2, 1); // A->C
    addEdge(2, 1, 2); // C->B
    addEdge(2, 3, 5); // C->D
    addEdge(1, 3, 1); // B->D
    addEdge(3, 4, 3); // D->E

    vector<long long> dist = dijkstra(n, 0, adj);

    vector<string> names = {"A","B","C","D","E"};
    for (int i = 0; i < n; i++)
        cout << names[i] << ": " << dist[i] << "\n";

    return 0;
}
```

### 7.2 C (qo'lda yozilgan min-heap bilan)

C tilida standart priority_queue yo'q, shuning uchun oddiy massiv asosidagi **O(V²)** yondashuvni ko'rsatamiz — bu tushunish uchun eng sodda usul:

```c
#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define V 5
#define INF INT_MAX

int minDistance(int dist[], bool visited[]) {
    int min = INF, minIndex = -1;
    for (int v = 0; v < V; v++) {
        if (!visited[v] && dist[v] <= min) {
            min = dist[v];
            minIndex = v;
        }
    }
    return minIndex;
}

void dijkstra(int graph[V][V], int source) {
    int dist[V];
    bool visited[V] = {false};

    for (int i = 0; i < V; i++)
        dist[i] = INF;
    dist[source] = 0;

    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, visited);
        if (u == -1) break; // qolgan tugunlar qaytmaydi
        visited[u] = true;

        for (int v = 0; v < V; v++) {
            if (!visited[v] && graph[u][v] != 0 &&
                dist[u] != INF &&
                dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    char names[] = {'A','B','C','D','E'};
    for (int i = 0; i < V; i++)
        printf("%c: %d\n", names[i], dist[i]);
}

int main() {
    // 0=A, 1=B, 2=C, 3=D, 4=E; 0 = qirra yo'q
    int graph[V][V] = {
        {0, 4, 1, 0, 0},
        {0, 0, 0, 1, 0},
        {0, 2, 0, 5, 0},
        {0, 0, 0, 0, 3},
        {0, 0, 0, 0, 0}
    };

    dijkstra(graph, 0);
    return 0;
}
```

### 7.3 Python (heapq bilan)

```python
import heapq

def dijkstra(n, source, adj):
    """
    n: tugunlar soni
    source: manba tugun indeksi
    adj: adj[u] = [(v, w), ...] — u dan v ga w og'irlik bilan qirra
    """
    dist = [float('inf')] * n
    dist[source] = 0
    visited = [False] * n

    pq = [(0, source)]  # (masofa, tugun)

    while pq:
        d, u = heapq.heappop(pq)

        if visited[u]:
            continue  # eskirgan yozuv
        visited[u] = True

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


if __name__ == "__main__":
    n = 5  # A=0, B=1, C=2, D=3, E=4
    adj = [[] for _ in range(n)]

    def add_edge(u, v, w):
        adj[u].append((v, w))

    add_edge(0, 1, 4)  # A->B
    add_edge(0, 2, 1)  # A->C
    add_edge(2, 1, 2)  # C->B
    add_edge(2, 3, 5)  # C->D
    add_edge(1, 3, 1)  # B->D
    add_edge(3, 4, 3)  # D->E

    dist = dijkstra(n, 0, adj)

    names = ["A", "B", "C", "D", "E"]
    for i in range(n):
        print(f"{names[i]}: {dist[i]}")
```

**Barcha uch implementatsiya ham yuqoridagi jadvaldagi natijani beradi:** A:0, B:3, C:1, D:4, E:7.

## 8. Muhim nozik jihatlar (Edge Cases va Optimizatsiyalar)

1. **`if (visited[u]) continue;` nega kerak?** Priority queue'ga bitta tugun uchun bir necha marta (turli `dist` qiymatlari bilan) yozuv qo'shilishi mumkin (chunki biz eski yozuvni o'chirib tashlamaymiz, faqat yangisini qo'shamiz — bu **"lazy deletion"** deb ataladi). Shu sababli, navbatdan chiqarilganda, agar tugun allaqachon yakunlangan bo'lsa, uni qayta ishlashning hojati yo'q.

2. **Yetib bo'lmaydigan tugunlar:** Agar biror tugun manbadan yetib bo'lmasa, uning `dist` qiymati `infinity` bo'lib qoladi.

3. **Yo'lni tiklash (Path reconstruction):** Agar shunchaki masofa emas, balki **eng qisqa yo'lning o'zi** kerak bo'lsa, qo'shimcha `parent[]` massivi yuritiladi: har safar `dist[v]` yangilanganda, `parent[v] = u` deb belgilanadi. Oxirida `E`dan `parent` orqali orqaga qaytib, yo'lni tiklash mumkin.

4. **Manfiy og'irliklar bilan nima bo'ladi?** Dijkstra **noto'g'ri** natija beradi. Bunday holatda **Bellman-Ford** (O(VE)) yoki manfiy sikl yo'q bo'lsa **Johnson's algorithm** ishlatiladi.

## 9. Boshqa algoritmlar bilan taqqoslash

| Algoritm | Manfiy og'irlik? | Vaqt murakkabligi | Qachon ishlatiladi |
|---|---|---|---|
| **Dijkstra** | Yo'q | O((V+E) log V) | Manfiy bo'lmagan og'irliklar, single-source |
| **Bellman-Ford** | Ha | O(VE) | Manfiy og'irliklar mumkin, manfiy sikl aniqlash |
| **Floyd-Warshall** | Ha (sikl bo'lmasa) | O(V³) | Barcha juftliklar orasidagi masofa (all-pairs) |
| **BFS** | Og'irliksiz (unweighted) | O(V+E) | Barcha qirralar og'irligi bir xil bo'lsa |
| **A\*** | Yo'q (heuristika bilan) | Dijkstra'dan tezroq (amalda) | Bitta maqsad nuqta ma'lum bo'lganda |

## 10. Mashq uchun tavsiya etilgan masalalar

Tushunchani mustahkamlash uchun quyidagi turdagi masalalarni yechib ko'rish tavsiya etiladi:
- Oddiy shortest path (berilgan graf, A dan Z gacha)
- Modifikatsiyalangan Dijkstra: eng qisqa yo'llar sonini hisoblash
- Ikkinchi eng qisqa yo'l (second shortest path) topish
- 0-1 BFS (og'irliklar faqat 0 va 1 bo'lganda, deque bilan optimallashtirish)
- Grid-based shortest path (matritsa ko'rinishidagi graf)

---

**Xulosa:** Dijkstra algoritmi — greedy strategiya va priority queue'ning kombinatsiyasi orqali manfiy bo'lmagan og'irlikdagi graflarda eng qisqa yo'lni samarali topadigan klassik algoritm. Uning asosini tushunish — grafik algoritmlar dunyosiga kirish uchun poydevor hisoblanadi.
