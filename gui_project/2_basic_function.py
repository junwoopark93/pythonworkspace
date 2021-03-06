import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Memojang")


# 파일 추가
def add_file():
    pass

# 선택 삭제
def del_file():
    pass


#file frame
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,text="파일 추가", command=add_file)
btn_add_file.pack(side="left", padx=3, pady=3)

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right", padx=3, pady=3)


#list frame
list_frame = Frame(root)
list_frame.pack(fill="both",padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y", padx=3, pady=3)

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True, padx=3, pady=3)
scrollbar.config(command=list_file.yview)


# save path frame
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x",padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=3, pady=3)


#option frame

frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

#가로 넓이 label
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=3, pady=3)

#가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=3, pady=3)

#간격 옵션 label
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=3, pady=3)

#간격 옵션 콤보

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=3, pady=3)

#파일포맷 옵션 label
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=3, pady=3)

#파일포맷 옵션 콤보

opt_format = ["없음", "좁게", "보통", "넓게"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=3, pady=3)

# 진행상황 progressbar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=3, pady=3, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=3, pady=3)

#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x",padx=5, pady=5, ipady=5)

btn_close = Button(frame_run,padx=5, pady=5, text="닫기",width=12, command=root.quit)
btn_close.pack(side="right", padx=3, pady=3)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right", padx=3, pady=3)


root.resizable(False, False)

root.mainloop()