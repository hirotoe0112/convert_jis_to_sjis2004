# 参考：https://ja.wikipedia.org/wiki/Shift_JIS-2004
def calculate_s1(m, k):
    if m == 1:
        if 1 <= k <= 62:
            return (k + 0x101) // 2
        elif 63 <= k <= 94:
            return (k + 0x181) // 2
    elif m == 2:
        if k in {1, 3, 4, 5, 8, 12, 13, 14, 15}:
            return (k + 0x1DF) // 2 - (k // 8) * 3
        elif 78 <= k <= 94:
            return (k + 0x19B) // 2
    return None


def calculate_s2(k, t):
    if k % 2 == 1:  # k が奇数の場合
        if 1 <= t <= 63:
            return t + 0x3F
        elif 64 <= t <= 94:
            return t + 0x40
    else:  # k が偶数の場合
        return t + 0x9E
    return None


def jis_to_sjis(m, k, t):
    s1 = calculate_s1(m, k)
    s2 = calculate_s2(k, t)

    if s1 is None or s2 is None:
        raise ValueError("Invalid input for JIS to Shift JIS conversion.")

    return s1, s2


def sjis_to_unicode(s1, s2):
    """
    Shift JISのバイト列をUnicode文字に変換する関数。
    :param s1: Shift JISの第1バイト
    :param s2: Shift JISの第2バイト
    :return: Unicode文字列
    """
    sjis_bytes = bytearray([s1, s2])
    return sjis_bytes.decode("sjis_2004")


"""
# サンプルの入力
m = 2
k = 1
t = 6

try:
    s1, s2 = jis_to_sjis(m, k, t)
    print(f"面番号: {m}, 区番号: {k}, 点番号: {t}")
    print(f"Shift JIS 第1バイト: {s1:02X}, 第2バイト: {s2:02X}")

    # Shift JISバイト列を文字に変換
    unicode_char = sjis_to_unicode(s1, s2)
    print(f"Shift JISコード ({s1:02X}, {s2:02X}) -> Unicode文字: {unicode_char}")

except (UnicodeDecodeError, ValueError) as e:
    print(f"変換エラー: {e}")
"""
