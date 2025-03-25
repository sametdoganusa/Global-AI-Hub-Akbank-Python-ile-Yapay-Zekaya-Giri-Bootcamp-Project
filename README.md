# 🚇 Samet Doğan - Sürücüsüz Metro Simülasyonu

Bu proje, Global AI Hub & Akbank Python ile Yapay Zekaya Giriş Bootcamp kapsamında hazırlanmıştır. Gerçek hayattaki metro sistemlerinde, iki istasyon arasında en hızlı ya da en az aktarmalı rotayı bulmak gibi sorunlara algoritmalarla çözüm geliştirmek hedeflenmiştir.

Python diliyle geliştirilen bu projede hem graf yapısı oluşturulmuş hem de iki farklı algoritma uygulanmıştır. Kodlar, `SametDogan_MetroSimulation.py` dosyasında bulunmaktadır.

---

## 🎯 Proje Amacı

PDF dosyasında belirtilen amaçlar doğrultusunda proje aşağıdaki hedefleri gerçekleştirmiştir:

1. Metro istasyonları ve hatları graf yapısı ile modellenmiştir.
2. En az aktarmalı rota için BFS (Breadth-First Search) algoritması uygulanmıştır.
3. En kısa süreli rota için A* (A Star) algoritması kullanılmıştır.
4. Kod içerisinde istasyonlar, bağlantılar ve test senaryoları örneklenmiştir.

---

## ⚙️ Kullanılan Teknolojiler ve Kütüphaneler

- Python 3
- `collections` (deque, defaultdict): Kuyruk ve hat listeleri için
- `heapq`: A* algoritmasında öncelik kuyruğu için
- `itertools.count`: A* algoritmasında sıra karışmaması için sayaç
- `typing`: Kodun anlaşılabilirliğini artırmak için

---

## 📌 Algoritma Özeti

### 1. BFS (en_az_aktarma_bul)
- Kuyruk kullanarak istasyonlar arasında en az duraklı yol bulunur.
- Daha önce ziyaret edilen istasyonlar tekrar edilmez.
- İlk hedefe ulaşıldığında döngü durur.

### 2. A* (en_hizli_rota_bul)
- Öncelik kuyruğu kullanılır.
- Her adımda `f = g + h` hesabı yapılır.
  - `g`: Gerçekten gidilen süre
  - `h`: Heuristic (aynı hat 2 dk, farklı hat 5 dk gibi basit tahmin)
- En mantıklı yol öncelikle işlenir.

---

## 🧱 Projenin Kodu

- `Istasyon` sınıfı: Bir istasyonun ID, adı, hattı ve komşuları vardır.
- `MetroAgi` sınıfı: Tüm istasyonları ve bağlantıları içerir. Algoritmalar bu sınıf içinde tanımlanmıştır.

Örnek kullanım:
```python
rota = metro.en_az_aktarma_bul("M1", "K4")
rota, sure = metro.en_hizli_rota_bul("M1", "K4")
```

---

## 🔍 Test Sonuçları

### AŞTİ → OSB
- En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
- En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB

### Batıkent → Keçiören
- En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
- En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

### Keçiören → AŞTİ
- En az aktarmalı rota: Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
- En hızlı rota (17 dakika): Keçiören -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

---

## 💡 Geliştirme Fikirleri

- Gerçek metro verisiyle çalışmak (örneğin İstanbul metrosu)
- Grafik arayüz eklemek (örneğin Streamlit)
- Kullanıcının başlangıç ve hedef istasyon girerek arama yapması

---

## 📁 Dosya Yapısı
```
SametDogan_MetroSimulation/
├── SametDogan_MetroSimulation.py
├── README.md
```

---

## 🚀 Çalıştırma

1. Python 3 kurulu olduğundan emin olun.
2. Terminal veya komut satırından çalıştırın:
```bash
python SametDogan_MetroSimulation.py
```
3. Çıktılar terminalde görüntülenecektir.

---


**Samet Doğan**  
Global AI Hub x Akbank Python Bootcamp Katılımcısı

---

Teşekkürler! 🙌

