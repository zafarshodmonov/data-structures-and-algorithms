# Binary Tree

## Traversal A Tree

```python
traversal = {
    0: "root",
    1: "left",
    2: "right"
}

"""
pre_order: (0, 1, 2)
in__order: (1, 0, 2)
postorder: (1, 2, 0)
"""
```

Daraxtni aylanib o'tish - Kirish

Muammo haqida xabar berish
Traversalga oldindan buyurtma bering
Tartib bo'yicha o'tish
Buyurtmadan keyingi sayohat
Rekursiv yoki iterativ

Traversalga oldindan buyurtma bering
Oldindan buyurtma berish - bu birinchi navbatda ildizga tashrif buyurishdir. Keyin chap pastki daraxtdan o'ting. Nihoyat, o'ng pastki daraxtni kesib o'ting. Mana bir misol:

Eslatma: quyidagi animatsiyada qizil rang bilan ajratib ko'rsatish biz tugun tashrifidan qaytganimizni bildiradi. Tashrif tartibi ikkilik daraxt ostidagi massivda ko'rsatilgan.

Hozirgi
1/19
Tartib bo'yicha o'tish
Tartib bo'yicha o'tish - avval chap pastki daraxtni kesib o'tish. Keyin ildizga tashrif buyuring. Nihoyat, o'ng pastki daraxtni kesib o'ting.

Keling, birgalikda harakat qilaylik:

Hozirgi
22 / 22
Odatda, uchun binary search tree, biz tartib bo'yicha o'tish yordamida barcha ma'lumotlarni tartiblangan tartibda olishimiz mumkin. Buni yana bir kartada eslatib o'tamiz ( Ma'lumotlar tuzilishiga kirish - Ikkilik qidiruv daraxti ).

Buyurtmadan keyingi sayohat
Buyurtmadan keyingi o'tish - avval chap pastki daraxtni kesib o'tish. Keyin o'ng pastki daraxtni kesib o'ting. Nihoyat, ildizga tashrif buyuring.

Buyurtmadan keyingi harakatni tushunishingizga yordam beradigan animatsiya:

Hozirgi
1/19
Shuni ta'kidlash kerakki, siz daraxtdagi tugunlarni o'chirsangiz, o'chirish jarayoni keyingi tartibda bo'ladi. Ya'ni, tugunni o'chirganingizda, tugunni o'chirishdan oldin uning chap va o'ng bolasini o'chirasiz.

Shuningdek, keyingi tartib matematik ifodalarda keng qo'llaniladi. Buyurtmadan keyingi ifodani tahlil qilish uchun dastur yozish osonroq. Mana bir misol:

Tartibni kesib o'tish orqali asl ifodani osongina aniqlashingiz mumkin. Biroq, dastur uchun bu ifodani boshqarish oson emas, chunki siz operatsiyalarning ustuvorligini tekshirishingiz kerak.

Agar siz ushbu daraxtni postorderda ishlatsangiz, stek yordamida ifodani osongina boshqarishingiz mumkin. Har safar operator bilan uchrashganingizda, siz stekdan 2 ta elementni chiqarib olishingiz, natijani hisoblashingiz va natijani stekga qaytarishingiz mumkin.

Rekursiv yoki iterativ
Maqoladan keyingi mashg'ulotimizda uch xil o'tish usulini qo'llashga harakat qiling. Usullarni rekursiv yoki iterativ tarzda amalga oshirishni xohlashingiz mumkin. Rekursiya va iteratsiya yechimlarini amalga oshiring va ular orasidagi farqlarni solishtiring.
