import tkinter as tk

# 메인 윈도우 생성
window = tk.Tk()
window.title("메모장")
window.geometry("600x400")

# --- 메뉴바 생성 ---

# 1. 메뉴바의 가장 바깥 틀을 생성합니다.
menubar = tk.Menu(window)

# 2. '파일' 드롭다운 메뉴를 생성합니다. (tearoff=0은 메뉴가 분리되지 않게 합니다)
file_menu = tk.Menu(menubar, tearoff=0)

# 3. '파일' 메뉴에 각 항목을 추가합니다.
#    - add_command: 메뉴 항목을 추가합니다.
#    - add_separator: 구분선을 추가합니다.
file_menu.add_command(label="새로만들기")
file_menu.add_command(label="열기")
file_menu.add_command(label="저장")
file_menu.add_command(label="다른이름으로 저장")
file_menu.add_separator()
file_menu.add_command(label="종료", command=window.quit)

# 4. 메뉴바에 '파일' 메뉴를 '파일'이라는 이름으로 추가합니다.
menubar.add_cascade(label="파일", menu=file_menu)

# 5. 윈도우의 메뉴로 위에서 만든 메뉴바를 설정합니다.
window.config(menu=menubar)

# 화면 중앙에 텍스트를 표시하기 위한 라벨(Label) 생성
# font 옵션으로 글꼴과 크기를 지정할 수 있습니다.
label = tk.Label(window, text="메모장을 만들어봐요", font=("맑은 고딕", 16))

# 윈도우를 화면에 표시
window.mainloop()


