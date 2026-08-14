"""
Renderizador genérico de carrosséis.
Uso:
    python render.py <slides.html> <pasta_saida> <prefixo>
Deteta automaticamente todos os <div class="slide" id="sN"> e exporta cada um
para PNG (2x) e junta tudo num PDF. Não é preciso indicar o número de slides.
Requer: playwright + Pillow  (pip install playwright Pillow ; playwright install chromium)
"""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image

def main():
    if len(sys.argv) < 4:
        print("uso: python render.py <slides.html> <pasta_saida> <prefixo>")
        sys.exit(1)
    html = os.path.abspath(sys.argv[1])
    outdir = os.path.abspath(sys.argv[2])
    prefix = sys.argv[3]
    os.makedirs(outdir, exist_ok=True)

    pngs = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1080}, device_scale_factor=2)
        page.goto("file:///" + html.replace("\\", "/"))
        page.wait_for_timeout(500)
        try:
            page.evaluate("document.fonts.ready")
        except Exception:
            pass
        page.wait_for_timeout(1200)
        # detetar todos os ids dos slides pela ordem do documento
        ids = page.eval_on_selector_all(".slide", "els => els.map(e => e.id)")
        if not ids:
            print("ERRO: nenhum elemento .slide encontrado no HTML.")
            sys.exit(2)
        for sid in ids:
            out = os.path.join(outdir, f"{prefix}_{sid}.png")
            page.locator("#" + sid).screenshot(path=out)
            pngs.append(out)
            print("ok", out)
        browser.close()

    imgs = [Image.open(x).convert("RGB") for x in pngs]
    pdf = os.path.join(outdir, f"{prefix}.pdf")
    imgs[0].save(pdf, save_all=True, append_images=imgs[1:])
    print("PDF", pdf)
    print("SLIDES", len(pngs))

if __name__ == "__main__":
    main()
