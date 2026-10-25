"""Animasi hati berdetak di terminal. Jalankan: python love.py  (Ctrl+C untuk berhenti)"""
import math
import os
import sys
import time

NAMA = sys.argv[1] if len(sys.argv) > 1 else "Kamu"
W, H = 60, 26
COLORS = [196, 197, 198, 204, 210, 217]  # gradasi merah -> pink (ANSI 256)


def inside(x, y):
    # persamaan hati: (x^2 + y^2 - 1)^3 - x^2 * y^3 <= 0
    return (x * x + y * y - 1) ** 3 - x * x * y ** 3 <= 0


def frame(t):
    beat = 1 + 0.08 * max(0, math.sin(t * 5)) ** 6 + 0.03 * math.sin(t * 2)
    rows = []
    for j in range(H):
        line = ""
        for i in range(W):
            x = (i - W / 2) / (W / 2) * 1.5 / beat
            y = -(j - H / 2) / (H / 2) * 1.4 / beat + 0.1
            if inside(x, y):
                shade = min(int((1 - (y + 1.2) / 2.4) * len(COLORS)), len(COLORS) - 1)
                shade = max(shade, 0)
                line += f"\033[38;5;{COLORS[shade]}m\u2588\033[0m"
            else:
                line += " "
        rows.append(line)
    text = f"Untuk {NAMA} \u2764"
    pad = " " * ((W - len(text)) // 2)
    rows.append("")
    rows.append(f"{pad}\033[1;38;5;218m{text}\033[0m")
    return "\n".join(rows)


def main():
    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.write("\033[?25l")  # sembunyikan kursor
    try:
        t = 0.0
        while True:
            sys.stdout.write("\033[H" + frame(t))
            sys.stdout.flush()
            t += 0.05
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h\n")


if __name__ == "__main__":
    main()
