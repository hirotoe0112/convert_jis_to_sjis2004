from tkinter import *
from convert import *


def on_entry_change(*args):
    text = str(jis_text.get())
    print(text)
    if len(text) == 5:
        # textの1文字目をm、2文字目から3文字目をk、4文字目から5文字目をtに変換
        m = int(text[0])
        k = int(text[1:3])
        t = int(text[3:5])
        print(m)
        print(k)
        print(t)
        try:
            s1, s2 = jis_to_sjis(m, k, t)
            print(f"面番号: {m}, 区番号: {k}, 点番号: {t}")
            print(f"Shift JIS 第1バイト: {s1:02X}, 第2バイト: {s2:02X}")

            # Shift JISバイト列を文字に変換
            unicode_char = sjis_to_unicode(s1, s2)
            print(
                f"Shift JISコード ({s1:02X}, {s2:02X}) -> Unicode文字: {unicode_char}"
            )
            result_entry.delete(0, END)
            result_entry.insert(0, unicode_char)

        except (UnicodeDecodeError, ValueError) as e:
            print(f"変換エラー: {e}")


def copy_to_clipboard(event):
    window.clipboard_clear()
    window.clipboard_append(result_entry.get())
    result_entry.select_range(0, END)


window = Tk()
window.title("Convert from JIS to SJIS2004")
window.config(padx=20, pady=20)

jis_text = StringVar()
jis_text.trace_add("write", on_entry_change)

jis_entry = Entry(width=20, font=("Arial", 30), textvariable=jis_text)
jis_entry.focus()
jis_entry.bind("<FocusIn>", lambda event: jis_entry.select_range(0, END))
jis_entry.grid(column=0, row=0)

result_entry = Entry(width=3, font=("Arial", 80))
result_entry.bind("<FocusIn>", copy_to_clipboard)
result_entry.grid(column=0, row=1, pady=20)

window.mainloop()
