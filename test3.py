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

# '편집' 드롭다운 메뉴를 생성합니다.
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="실행 취소")
edit_menu.add_command(label="다시 실행")
edit_menu.add_separator()
edit_menu.add_command(label="잘라내기")
edit_menu.add_command(label="복사")
edit_menu.add_command(label="붙여넣기")
edit_menu.add_separator()
edit_menu.add_command(label="모두 선택")

# 메뉴바에 '편집' 메뉴를 '편집'이라는 이름으로 추가합니다.
menubar.add_cascade(label="편집", menu=edit_menu)

# 5. 윈도우의 메뉴로 완성된 메뉴바를 설정합니다.
window.config(menu=menubar)

# 윈도우를 화면에 표시
window.mainloop()



