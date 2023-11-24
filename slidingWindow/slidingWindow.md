# Whats is Sliding Window?

The sliding window technique is a method used for efficiently processing arrays or lists by maintaining a subset of elements within a fixed-size "window" that slides through the entire data structure. This technique is particularly useful for solving problems involving subarrays, subsequences, or intervals.

The key idea behind the sliding window is to maintain a set of elements while iterating through the array or list, and as the window slides, update the set efficiently by adding new elements and removing old ones. This allows for a more optimized and linear-time solution to problems that might otherwise require nested loops.

Here are the general steps involved in the sliding window technique:

1. **Initialization**: Set up the initial window by defining its size and initializing any necessary variables.

2. **Process Initial Window**: Perform any required operations or calculations for the elements within the initial window.

3. **Slide the Window**: Move the window one step at a time through the array or list.

4. **Update the Window**: As the window slides, efficiently update the set of elements by adding the new element entering the window and removing the old element leaving the window.

5. **Process Current Window State**: Perform any required operations or calculations for the elements within the current window.

6. **Repeat**: Continue sliding the window until it reaches the end of the array or list.

The sliding window technique is often used to solve problems related to finding subarrays or subsequences that satisfy specific conditions, such as maximizing or minimizing a sum, finding the longest subarray with distinct elements, or solving problems involving intervals.

Let's consider an example to illustrate the sliding window technique:

**Example: Maximum Sum Subarray of Size K**
Given an array of integers and a positive integer K, find the maximum sum of a subarray of size K.

```python
def max_sum_subarray(arr, k):
    n = len(arr)
    
    # Initialize the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window through the array
    for i in range(n - k):
        # Add the new element and subtract the old element
        window_sum = window_sum - arr[i] + arr[i + k]
        # Update the maximum sum
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 3
result = max_sum_subarray(arr, k)
print(result)  # Output: 21
```

In this example, the sliding window of size `K` is moved through the array, and at each step, the sum of the subarray within the window is calculated. The maximum sum encountered during the process is the answer to the problem.

## 'Siljuvchi Oyna Texnikasi' nima?

'Siljuvchi Oyna Texnikasi' - bu butun ma'lumotlar strukturasi bo'ylab siljiydigan qattiq o'lchamdagi "oyna" ichidagi elementlarning kichik to'plamini saqlab, massivlar yoki ro'yxatlarni samarali qayta ishlash uchun ishlatiladigan usul. Ushbu uslub, ayniqsa, pastki qatorlar, pastki ketma-ketliklar yoki intervallar bilan bog'liq muammolarni hal qilish uchun foydalidir.

'Siljuvchi Oyna' ortidagi asosiy g'oya massiv yoki ro'yxat bo'ylab takrorlanayotganda elementlar to'plamini saqlab qolish va oyna siljiganida yangi elementlarni qo'shish va eskilarini olib tashlash orqali to'plamni samarali yangilashdir. Bu ichki halqalarni talab qilishi mumkin bo'lgan muammolarni yanada optimallashtirilgan va chiziqli vaqt ichida hal qilish imkonini beradi.

'Siljuvchi Oyna Texnikasi' bilan bog'liq umumiy qadamlar:

1. **Initializatsiya**: Dastlabki oynani uning hajmini aniqlash va kerakli o'zgaruvchilarni ishga tushirish orqali o'rnating.

2. **Jarayonning dastlabki oynasi**: Dastlabki oyna ichidagi elementlar uchun kerakli amallar yoki hisob-kitoblarni bajaring.

3. **Oynani siljitish**: Oynani massiv yoki ro‘yxat bo‘ylab bir qadam siljiting.

4. **Oynani yangilash**: Oyna siljishi bilan oynaga kiruvchi yangi elementni qo‘shish va oynadan chiqayotgan eski elementni olib tashlash orqali elementlar to‘plamini samarali yangilang.

5. **Joriy oyna holatini qayta ishlash**: Joriy oyna ichidagi elementlar uchun kerakli amallar yoki hisob-kitoblarni bajaring.

6. **Takrorlash**: Oynani massiv yoki ro‘yxat oxirigacha siljitishda davom eting.

'Siljuvchi Oyna Texnikasi' ko'pincha yig'indini maksimallashtirish yoki minimallashtirish, alohida elementlarga ega eng uzun pastki qatorni topish yoki intervallar bilan bog'liq muammolarni hal qilish kabi muayyan shartlarni qondiradigan pastki qatorlar yoki pastki qatorlarni topish bilan bog'liq muammolarni hal qilish uchun ishlatiladi.

'Siljuvchi Oyna Texnikasini' tasvirlash uchun misolni ko'rib chiqaylik:

**Masalan: K o'lchamdagi maksimal yig'indi qatori**
Butun sonlar massivi va K musbat butun son berilgan bo‘lsa, K o'lchamli pastki massivning maksimal yig'indisini toping.

```python
def max_sum_subarray(arr, k):
    n = len(arr)
    
    # Initialize the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window through the array
    for i in range(n - k):
        # Add the new element and subtract the old element
        window_sum = window_sum - arr[i] + arr[i + k]
        # Update the maximum sum
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 3
result = max_sum_subarray(arr, k)
print(result)  # Output: 21
```

Bu misolda `K` o'lchamdagi suriluvchi oyna massiv bo'ylab ko'chiriladi va har bir qadamda oyna ichidagi pastki qator yig`indisi hisoblanadi. Jarayon davomida duch kelgan maksimal summa muammoning javobidir.
