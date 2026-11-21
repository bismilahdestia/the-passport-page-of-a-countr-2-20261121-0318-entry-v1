# The Passport Page of a Country That Isn't There
# (the-passport-page-of-a-countr-2-20261121-0318, v1).
#
# An open passport spread for the invented Republic of Valdoria:
# left page = data page (portrait of Elena Marovic, bilingual
# Valdorian/English fields, MRZ with real ICAO check digits);
# right page = a Tarnovia business visa sticker (single entry,
# 28 Mar - 27 Apr 2026, no employment, 40 koruna fee paid) plus
# ten entry/exit stamps telling one coherent travel history.
# Every stamp is dated after the passport's issue (12 Mar 2026)
# and the trips run in order: Marovel -> Velgrad (Tarnovia) ->
# Port Sarn (Sarnia) -> Marovel, then Marovel -> Velgrad ->
# Marovel again. Nothing predates the passport; no date
# contradicts the place of issue.
#
# The image itself is entry.png beside this file (drawn once,
# offline, with Pillow + DejaVu fonts by render.py outside the
# repo). The program's only job is to place that exact image at
# /output/entry.png for the grader, byte for byte, on every run
# -- and to verify the copied bytes match the source before
# finishing, failing loudly on any mismatch instead of handing
# the grader a corrupted copy. Pure standard library: the
# grading sandbox runs vanilla Python 3.13 with no network.
#
# Run it outside the grader's container with:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, dest)

    # Verify the copy before finishing: the grader gets entry.png
    # byte for byte, so a silent short or corrupted write must
    # fail loudly.
    with open(SRC, "rb") as f:
        src_bytes = f.read()
    with open(dest, "rb") as f:
        dest_bytes = f.read()
    if src_bytes != dest_bytes:
        sys.exit(
            "entry.png copy mismatch: source %d bytes, copied %d bytes"
            % (len(src_bytes), len(dest_bytes))
        )
    print("wrote %s (%d bytes)" % (dest, len(dest_bytes)))


if __name__ == "__main__":
    main()
