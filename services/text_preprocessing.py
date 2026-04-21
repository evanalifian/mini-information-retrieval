from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


class TextPreprocessing:
    tokens = {}

    def __init__(self, query, docs):
        self.__stopwords = [
            "yang","dan","di","ke","dari","pada","untuk","dengan","sebagai","adalah",
            "itu","ini","atau","karena","oleh","dalam","terhadap","antara","tanpa",
            "juga","agar","sehingga","namun","tetapi","lalu","kemudian","bahwa",
            "saat","ketika","sebelum","sesudah","setelah","selama","hingga","yaitu",
            "yakni","dapat","akan","harus","telah","sudah","belum","masih","lagi",
            "lebih","kurang","sangat","cukup","banyak","sedikit","semua","beberapa",
            "masing","setiap","para","seorang","seseorang","sesuatu",
            "penelitian","hasil","metode","data","analisis","studi","artikel",
            "jurnal","penulis","responden","variabel","pengaruh","hubungan",
            "berdasarkan","menunjukkan","diketahui","digunakan","dilakukan",
            "diperoleh","terdapat","memiliki","menggunakan","memberikan",
            "menjadi","terjadi","berupa","melalui","tersebut",
            "hal","cara","jenis","bagian","fungsi","proses","kondisi",
            "tingkat","jumlah","nilai","tahun","hari","bulan","waktu",
            "tempat","wilayah","daerah","lingkungan","kegiatan",
            "masalah","solusi","tujuan","manfaat"
        ]
        self.__query = query
        self.__docs = docs

    def tokenization(self):
        self.tokens = {"q": self.__query.split()}

        for doc, word in zip(self.__docs.keys(), self.__docs.values()):
            self.tokens[doc] = word.split()

    def case_folding(self):
        for key, token in zip(self.tokens.keys(), self.tokens.values()):
            arr = []
            for word in token:
                arr.append(word.lower())
            self.tokens[key] = arr

    def stopword_removal(self):
        for key, token in zip(self.tokens.keys(), self.tokens.values()):
            for stopword in self.__stopwords:
                if stopword in token:
                    token.remove(stopword)
            self.tokens[key] = token

    def stemming(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        for key, token in zip(self.tokens.keys(), self.tokens.values()):
            words = " ".join(token)
            opt = stemmer.stem(words)
            self.tokens[key] = opt.split()

    def get_doc_length(self, doc):
        return len(doc)
