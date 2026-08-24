#!/usr/bin/env python3
"""Gera vídeo do carrossel 04 (slides PNG) para YouTube e TikTok, sem música."""
import os, subprocess, sys

FFMPEG = r"C:\Users\Sandra Lourenço\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin\ffmpeg.exe"
FOLDER = r"C:\Users\Sandra Lourenço\Downloads\carrosseis-ia\outputs\carrossel_04_niveis"
SLIDES = [os.path.join(FOLDER, f"carrossel_04_s{i}.png") for i in range(1, 10)]
SLIDE_SEC = 4.0
FADE = 0.3

def build(out_path, mode):
    """mode: 'square' (1080x1080) ou 'vertical' (1080x1920, fundo desfocado)."""
    if mode == "square":
        W = H = 1080
    else:
        W, H = 1080, 1920

    inputs = []
    for s in SLIDES:
        inputs += ["-loop", "1", "-t", str(SLIDE_SEC), "-i", s]

    parts = []
    if mode == "square":
        for i in range(9):
            parts.append(f"[{i}:v]scale={W}:{H},setsar=1,setpts=N/FRAME_RATE/TB[v{i}]")
    else:
        for i in range(9):
            # fundo: zoom para cobrir + desfoque
            parts.append(f"[{i}:v]scale=1920:1920,crop=1080:1920:420:0,setsar=1,boxblur=40,setpts=N/FRAME_RATE/TB[bg{i}]")
            # primeiro plano: slide inteiro contido
            parts.append(f"[{i}:v]scale=1080:1080,setsar=1,setpts=N/FRAME_RATE/TB[fg{i}]")
            parts.append(f"[bg{i}][fg{i}]overlay=0:420:setsar=1[v{i}]")

    # cadeia de xfade
    prev = "v0"
    for k in range(1, 9):
        off = round(k * (SLIDE_SEC - FADE), 3)
        nxt = f"x0{k}"
        parts.append(f"[{prev}][v{k}]xfade=transition=fade:duration={FADE}:offset={off}[{nxt}]")
        prev = nxt

    filter_complex = ";".join(parts)
    cmd = [FFMPEG, "-y", *inputs, "-filter_complex", filter_complex,
           "-map", f"[{prev}]", "-r", "30", "-c:v", "libx264",
           "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "medium",
           "-movflags", "+faststart", "-an", out_path]
    return cmd

def run(cmd, label):
    print(f"\n=== {label} ===")
    print(" ".join(cmd[:6]), "...", "(args omitidos)")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERRO:", r.stderr[-3000:])
        sys.exit(1)
    print(f"OK -> {label}")

if __name__ == "__main__":
    yt = os.path.join(FOLDER, "carrossel_04_youtube.mp4")
    tk = os.path.join(FOLDER, "carrossel_04_tiktok.mp4")
    run(build(yt, "square"), yt)
    run(build(tk, "vertical"), tk)
    print("\nConcluído.")
