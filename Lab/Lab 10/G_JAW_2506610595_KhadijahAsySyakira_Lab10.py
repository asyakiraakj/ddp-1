import tkinter as tk
from tkinter.colorchooser import askcolor
import tkinter.messagebox as tkmsg


# ========================================
# BAGIAN BONUS: BRUSH CLASSES
# ========================================
# Uncomment dan lengkapi untuk mendapatkan poin bonus!

# class PencilBrush:
#     """Brush untuk free drawing dengan titik-titik kecil"""
#     
#     def draw(self, canvas, x, y, color):
#         """
#         TODO BONUS: Implementasi PencilBrush
#         
#         Apa yang harus dilakukan?
#         1. Set radius = 2
#         2. Gambar oval kecil di posisi (x, y) dengan radius tersebut
#            Hint: canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color)
#         """
#         pass


# class EmojiBrush:
#     """Brush untuk menggambar emoji (contoh: bintang)"""
#     
#     def draw(self, canvas, x, y, color):
#         """
#         TODO BONUS: Implementasi EmojiBrush
#         
#         Apa yang harus dilakukan?
#         1. Set ukuran shape (misal: size = 8)
#         2. Buat list points untuk koordinat shape
#            Contoh untuk bintang 5 sudut:
#            points = [x, y-size, x+2, y-3, x+size, y-3, ...]
#         3. Gambar polygon dengan canvas.create_polygon(points, fill=color, outline=color)
#         
#         Tips: Anda bisa pakai shape lain (hati, kotak, segitiga, dll)
#         """
#         pass


# TODO BONUS: Tambahkan minimal 1 brush class lagi!
# Contoh: CircleBrush, SquareBrush, TriangleBrush, HeartBrush
# Copy struktur di atas dan sesuaikan implementasinya


# ========================================
# MAIN APPLICATION
# ========================================

class MyPaint(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Konfigurasi ukuran canvas dan button
        self.__canvas_w = 500
        self.__canvas_h = 500
        self.__btn_w = 10      # Lebar button
        self.__btn_h = 2       # Tinggi button
        self.__radius = 2      # Radius titik yang dihasilkan ketika canvas di-click
        self.__color = "#000000"   # Default: black

        # TODO BONUS: Uncomment untuk Duck Typing
        # Instansiasi brush objects
        # self.pencil_brush = PencilBrush()
        # self.emoji_brush = EmojiBrush()
        # self.xxx_brush = XxxBrush()  # Ganti dengan nama brush ketiga Anda

        # TODO BONUS: Uncomment untuk Duck Typing
        # Set brush yang sedang aktif (default: pencil)
        # self.current_brush = self.pencil_brush

        self.master.title("MyPaint")

        self.create_tools()
        self.create_canvas()
   
    def create_canvas(self):
        self.canvas = tk.Canvas(self, width=self.__canvas_w, height = self.__canvas_h, background= "white")

        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<Button-1>", self.on_drag)

        self.canvas.pack()

    """
    TODO #1: Membuat canvas dan binding events
    
    Apa yang dilakukan di method ini?
    1. Instansiasi sebuah object Canvas dengan:
        - width = self.__canvas_w
        - height = self.__canvas_h
        - background color = "white"
        - Simpan di self.canvas
    
    2. Bind canvas dengan method self.on_drag(), dengan event type
        "<B1-Motion>" agar bisa menggambar ketika mouse di-drag
    
    3. Bind canvas juga dengan self.on_drag(), dengan event type
        "<Button-1>" agar bisa menggambar ketika mouse di-click
    
    4. Jangan lupa pack() canvas ke self (frame)
    
    Hint:
    - canvas.bind("<EventType>", self.method_name)
    - canvas.pack()
    """
        
    pass
      
    def create_tools(self):
        #1
        self.frame_for_tools = tk.Frame(self)
        #2
        self.btn_color = tk.Button(self.frame_for_tools, text="Pilih Warna", width = self.__btn_w, height = self.__btn_h, foreground="white", background=self.__color)
        self.btn_color.pack(side=tk.LEFT)
        #3
        self.btn_color.bind("<ButtonRelease-1>", self.btn_color_clicked)

        #4
        self.btn_erase = tk.Button(self.frame_for_tools, text="Hapus Canvas", width = self.__btn_w, height = self.__btn_h, foreground="white", background=self.__color)
        self.btn_erase.pack(side=tk.LEFT)
        #5
        self.btn_erase.bind("<ButtonRelease-1>", self.btn_erase_clicked)

        #6
        self.frame_for_tools.pack()
        
    # ======================================================================
    # BUTTON SAVE
    # ======================================================================
    # Button ini sudah jadi, bisa langsung dipakai untuk save gambar

        self.btn_save = tk.Button(
            self.frame_for_tools,
            text="Save",
            width=self.__btn_w,
            height=self.__btn_h
        )
        self.btn_save.pack(side=tk.LEFT, padx=5)
        self.btn_save.bind("<ButtonRelease-1>", self.btn_save_clicked)

    """
    TODO #2: Membuat control panel dengan buttons

    Apa yang dilakukan di method ini?
    Prinsipnya adalah membuat dua buah button yang ada di atas canvas.

    1. Buat frame baru yang akan menjadi container di bagian atas canvas:
        
        self.frame_for_tools = tk.Frame(self)

    2. Buatlah button untuk "Pilih Warna":
        - text = "Pilih Warna"
        - width = self.__btn_w
        - height = self.__btn_h
        - foreground color (fg) = "white"
        - background color (bg) = self.__color
        (agar warna button berubah sesuai warna yang dipilih)
        - Simpan di self.btn_color
        - Pack ke self.frame_for_tools dengan side=tk.LEFT
        (agar button bisa bersebelahan horizontal)

    3. Bind button "Pilih Warna" dengan:
        - Event type: "<ButtonRelease-1>"
        - Event handler: self.btn_color_clicked

    4. Buatlah button untuk "Hapus Canvas":
        - text = "Hapus Canvas"
        - width = self.__btn_w
        - height = self.__btn_h
        - Simpan di self.btn_erase
        - Pack ke self.frame_for_tools dengan side=tk.LEFT

    5. Bind button "Hapus Canvas" dengan:
        - Event type: "<ButtonRelease-1>"
        - Event handler: self.btn_erase_clicked

    6. Jangan lupa pack() frame_for_tools ke self (frame)

    Hint:
    - button.bind("<EventType>", self.method_name)
    - button.pack(side=tk.LEFT) untuk horizontal alignment
    """
    pass


    # ======================================================================
    # TODO BONUS: Uncomment untuk Duck Typing
    # ======================================================================
    #
    # Tambahkan button untuk setiap brush yang Anda buat.
    # Contoh untuk PencilBrush:

    # self.btn_pencil = tk.Button(
    #     self.frame_for_tools,
    #     text="Pencil",
    #     width=self.__btn_w,
    #     command=self.select_pencil  # Gunakan command, bukan bind
    # )
    # self.btn_pencil.pack(side=tk.LEFT, padx=5)

    # TODO BONUS: Tambahkan button untuk EmojiBrush
    # TODO BONUS: Tambahkan button untuk brush ketiga Anda
   
   # ========================================
   # TODO BONUS: BRUSH SELECTION METHODS
   # ========================================
   # Uncomment dan lengkapi untuk Duck Typing
   
   # def select_pencil(self):
   #     """
   #     TODO BONUS: Switch ke PencilBrush
   #     Set self.current_brush = self.pencil_brush
   #     """
   #     pass
   
   # def select_emoji(self):
   #     """
   #     TODO BONUS: Switch ke EmojiBrush
   #     Set self.current_brush = self.emoji_brush
   #     """
   #     pass
   
   # TODO BONUS: Tambahkan method select untuk brush ketiga!
   
   # ========================================
   # EVENT HANDLERS
   # ========================================
   
    def on_drag(self, event):
        x, y = event.x, event.y
        r = self.__radius
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=self.__color, outline=self.__color)

    """
    TODO #3: Implementasi free drawing

    Apa yang harus dilakukan?
    Simple... Anda cukup membuat lingkaran kecil terus-menerus
    saat mouse di-drag atau di-click.

    UNTUK BAGIAN WAJIB:
    1. Ambil koordinat mouse: x = event.x, y = event.y
    2. Ambil radius: r = self.__radius
    3. Buat lingkaran dengan pusat (x, y) dan radius r
        Perhatikan bahwa pusat lingkaran haruslah (event.x, event.y)!
        
        Hint untuk lingkaran dengan pusat (x, y) dan radius r:
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color)

    4. Gunakan self.__color sebagai warna fill dan outline

    ---

    UNTUK BAGIAN BONUS (ganti implementasi di atas):
    Hapus kode di atas dan ganti dengan Duck Typing:

    self.current_brush.draw(self.canvas, event.x, event.y, self.__color)

    Ini adalah Duck Typing! Satu baris code, tapi behavior berbeda
    tergantung brush yang aktif. Tidak perlu if-elif untuk cek tipe!
    """
    pass
   
    def btn_color_clicked(self, event):
      """
      Event handler untuk button Pilih Warna
      """
      color_code = askcolor()
      if color_code[-1] is not None:
         self.__color = color_code[-1]
         self.btn_color["bg"] = self.__color
   
    def btn_erase_clicked(self, event):
      """
      Event handler untuk button Hapus Canvas
      """
      self.canvas.delete("all")
   
    def btn_save_clicked(self, event):
      """
      Event handler untuk button Save
      Fungsi: Menyimpan gambar di canvas ke file PostScript (.ps)
      """
      try:
         self.canvas.postscript(file="my_drawing.ps")
         tkmsg.showinfo(
               "Berhasil",
               "Gambar berhasil disimpan sebagai 'my_drawing.ps'"
         )
      except Exception as e:
         tkmsg.showerror(
               "Error",
               f"Gagal menyimpan gambar:\n{str(e)}"
         )


# ========================================
# MAIN PROGRAM
# ========================================
if __name__ == "__main__":
   myapp = MyPaint()
   myapp.master.mainloop()
