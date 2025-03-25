from collections import defaultdict, deque
from itertools import count
import heapq
from typing import Dict, List, Tuple, Optional

class Istasyon:
    """
    Bir metro istasyonunu temsil eder.
    """
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx  # İstasyon ID
        self.ad = ad    # İstasyon adı
        self.hat = hat  # İstasyonun ait olduğu hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (komsu_istasyon, sure)

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

    def __repr__(self):
        return f"{self.ad} ({self.hat}, ID: {self.idx})"

    def __eq__(self, other):
        return isinstance(other, Istasyon) and self.idx == other.idx

    def __hash__(self):
        return hash(self.idx)

class MetroAgi:
    """
    Metro ağı yapısı. İstasyonlar ve hatlar burada tutulur.
    """
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)
        self.sayac = count()  # A* sıralama çakışmalarını önlemek için

    def heuristic(self, istasyon1: Istasyon, istasyon2: Istasyon) -> int:
        """
        A* algoritması için sezgisel fonksiyon. Aynı hatta olmak avantajlıdır.
        """
        if istasyon1.idx == istasyon2.idx:
            return 0
        if istasyon1.hat == istasyon2.hat:
            return 2
        return 5

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        if istasyon1_id not in self.istasyonlar or istasyon2_id not in self.istasyonlar:
            raise ValueError(f"{istasyon1_id} veya {istasyon2_id} ID'li istasyon bulunamadı.")
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """
        BFS algoritması ile en az aktarmalı rotayı bulur.
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            raise ValueError("Başlangıç veya hedef istasyonu bulunamadı.")

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        if baslangic == hedef:
            return [baslangic]

        ziyaret_edildi = {baslangic}
        kuyruk = deque([(baslangic, [baslangic])])

        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            if mevcut == hedef:
                return yol
            for komsu, _ in mevcut.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, yol + [komsu]))
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """
        A* algoritması ile en hızlı rotayı bulur.
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            raise ValueError("Başlangıç veya hedef istasyonu bulunamadı.")

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        if baslangic == hedef:
            return [baslangic], 0

        pq = [(self.heuristic(baslangic, hedef), 0, next(self.sayac), baslangic, [baslangic])]
        ziyaret_edildi = {}

        while pq:
            f, g, _, mevcut, yol = heapq.heappop(pq)

            if mevcut == hedef:
                return yol, g

            if mevcut in ziyaret_edildi and ziyaret_edildi[mevcut] <= g:
                continue
            ziyaret_edildi[mevcut] = g

            for komsu, sure in mevcut.komsular:
                yeni_g = g + sure
                yeni_f = yeni_g + self.heuristic(komsu, hedef)
                heapq.heappush(pq, (yeni_f, yeni_g, next(self.sayac), komsu, yol + [komsu]))

        return None

# --------------------------- TEST SENARYOLARI ---------------------------

if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonları ekleme
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)

    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)

    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)

    # Aktarmalar
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)

    # Testler
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
