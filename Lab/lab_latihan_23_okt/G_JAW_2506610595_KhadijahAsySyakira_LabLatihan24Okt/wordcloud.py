
# Tugas Anda cukup implementasikan 3 buah fungsi: unique_words(doc), count_word(word, doc), word_freqs(doc)

import random
    
def stopwords():
    """ daftar kata-kata yang sering muncul, dan kurang berbobot """
    return set(['dan', 'di', 'yang', 'dari', 'and', \
            'pada', 'the', 'of', 'dengan', 'untuk', \
            'oleh', 'ke', 'ini', 'adalah', 'dalam', \
            'sebagai', 'serta', 'hingga', 'juga'])

def rand_color():
    """ fungsi untuk menghasilkan kode warna (RGB Hex) secara random """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

def unique_words(doc):
    unique = set(doc.lower().split())
    return unique
    """ 
    doc   : sebuah dokumen tekstual, dalam bentuk single string
    return: set/himpunan kata-kata unik yang sudah di-lowercase dari doc
    
    contoh:
    >>> unique_words("SAYA saya SAya PERGI PerGI")
    {'pergi', 'saya'}
    
    """
    pass
    
def count_word(word, doc):
    count = 0
    for words in doc.lower().split():
        if words == word.lower():
            count += 1
    
    return count

    """
    word : sebuah kata, dalam bentuk string
    doc  : sebuah dokumen tekstual, dalam bentuk single string
    
    word & doc di-lowercase terlebih dahulu.
    
    fungsi return integer, yang merepresentasikan berapa kali kata word muncul di doc
    
    Contoh:
    >>> count_word("SAya", "SAYA saya SaYA mau Saya Pintar")
    4
    
    """
    pass

def word_freqs(doc):
    ans = []
    unique = unique_words(doc)
    for words in unique:
        ans.append((words, count_word(words, doc)))
    return ans


    """     
    doc  : sebuah dokumen tekstual, dalam bentuk single string
    
    fungsi return list of tuples, yang merepresentasikan berapa kali sebuah kata
    (unik) muncul pada dokumen tekstual doc.
    
    contoh:
    >>> word_freqs("SAYA saya SaYA mau Saya Pintar dan pintar coding")
    [("saya", 4), ("mau", 1), ("dan", 1), ("pintar", 2), ("coding", 1)]
    
    >>> word_freqs("HALO halo HAlo Depok depok UI")
    [("ui", 1), ("halo", 3), ("depok", 2)]
    
    Anda bisa call fungsi unique_words(...) dan count_word(...) yang sudah
    Anda definisikan sebelumnya.
    
    """
    pass
    

   
if __name__ == "__main__":   
  nama_file = input("Nama file teks = ")
  nama_file_out = input("Nama file wordcloud (.html) = ")
  
  with open(nama_file, encoding='utf-8') as file,\
       open(nama_file_out, "w") as file_out:
       
      # baca seluruh isi file input as a single string 
      w_f = word_freqs(file.read())
      
      # urutkan kata-kata dari yang frekuensi yang tinggi ke paling rendah
      sorted_w_f = sorted(w_f, key=lambda x: x[1], reverse=True)
      
      # pilih top-50 kata yang paling sering muncul / frekuensi paling tinggi
      top_n_words = sorted_w_f[:50]
      
      # kocok kembali urutan kata --> mengapa?
      random.shuffle(top_n_words)
      
      # tulis ke file wordcloud yang berekstensi HTML
      print('<p style="text-align: center;">', file=file_out)
      for w, f in top_n_words:
          print(f'<span style="font-size: {f}px; font-weight: bold; margin: 5px; display: inline-block; color: {rand_color()};">{w}</span>', file=file_out)
      print('</p>', file=file_out)      
      print(f"File wordcloud {nama_file_out} berhasil dibuat. Silakan buka dengan browser!")
    
        