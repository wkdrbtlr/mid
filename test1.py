import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# 메인 윈도우 생성
window = tk.Tk()
window.title("메모장")
window.geometry("600x400")

# 화면 중앙에 텍스트를 표시하기 위한 라벨(Label) 생성
# font 옵션으로 글꼴과 크기를 지정할 수 있습니다.
label = tk.Label(window, text="메모장을 만들어봐요", font=("맑은 고딕", 16))

# 라벨을 창에 배치하고, expand=True 옵션으로 중앙에 위치시킵니다.
label.pack(expand=True)

# 윈도우를 화면에 표시
window.mainloop()
