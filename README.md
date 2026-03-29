# mystery_module

Kısa açıklama

`mystery_module.py` küçük bir yardımcı fonksiyon içerir: bir ikinci dereceden denklemin (ax² + bx + c = 0) köklerini hesaplamak için basit bir uygulama. Fonksiyon, diskriminant negatifse `None` döner; aksi halde iki kökü (çiftli) döndürür.

## Fonksiyonlar

### fn_x(a, b, c)

- Açıklama: Verilen katsayılarla ikinci dereceden denklemin köklerini hesaplar.
- Parametreler:
  - `a` (sayı): x²'nin katsayısı. (Not: `a` = 0 durumunda fonksiyon bölme hatası verir.)
  - `b` (sayı): x'in katsayısı.
  - `c` (sayı): sabit terim.
- Dönen değer:
  - Eğer diskriminant (d = b² - 4ac) negatifse: `None`.
  - Aksi halde: `(root1, root2)` şeklinde iki float değerden oluşan tuple.

- Davranış ayrıntıları / kenar durumları:
  - `a == 0` ise, fonksiyon şu an `ZeroDivisionError` ile sonuçlanır. Eğer `a == 0` desteklenmesi isteniyorsa (lineer denklemler için), ek bir kontrol ve farklı bir davranış eklenmelidir.
  - `d < 0` olduğunda karmaşık kökler döndürülmez; fonksiyon `None` verir. İsterseniz karmaşık sonuçlar için `cmath` kullanılarak değiştirebiliriz.

## Örnek kullanım

Python REPL veya bir script içinde:

```python
from mystery_module import fn_x

roots = fn_x(1, -3, 2)  # x^2 - 3x + 2 = 0
print(roots)  # Çıktı: (2.0, 1.0)

print(fn_x(1, 0, 1))    # Diskriminant < 0 => None

# Dikkat: a == 0 durumunda hata alırsınız
# print(fn_x(0, 2, -4))
```

## Önerilen iyileştirmeler

1. Tip ipuçları (type hints) ve docstring'lerin genişletilmesi.
2. `a == 0` durumu için kontrol ekleyip anlamlı bir davranış sağlanması (ör. ValueError fırlatma veya lineer denklemi çözme).
3. Negatif diskriminant için `None` yerine karmaşık kökler döndürmek isterseniz `cmath` kullanılabilir.
4. Birim testleri eklenmesi (pytest):
   - Normal durum (iki gerçek kök)
   - Tekrarlı kök (d == 0)
   - Negatif diskriminant (d < 0)
   - `a == 0` durumunun ele alınması

## Küçük geliştirilmiş örnek (öneri)

Aşağıdaki kısa snippet, `a == 0` için daha iyi hata mesajı ve tiplerin belirtildiği bir versiyon önerebilir:

```python
import math
from typing import Optional, Tuple

Number = float | int

def fn_x(a: Number, b: Number, c: Number) -> Optional[Tuple[float, float]]:
    if a == 0:
        raise ValueError("Parameter 'a' must not be zero for a quadratic equation")
    d = b**2 - 4*a*c
    if d < 0:
        return None
    sqrt_d = math.sqrt(d)
    return ((-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a))
```

## Lisans ve katkıda bulunma

Bu depo öğrenci projesi olarak gözüküyor. Değişiklik yapmak, hata düzeltmek veya test eklemek isterseniz lütfen yeni bir branch açıp PR gönderin.

---

Hazırda başka bir belge ya da örnek isterseniz ekleyebilirim: örneğin `tests/test_mystery_module.py` ile birkaç pytest durumu hazırlayayım mı?
