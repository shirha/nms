# -*- coding: utf-8 -*-
import cv2

def isGlyphs(glyph_image, decod_image):
    glyphs = ''
    for i in range(12):
        result = cv2.matchTemplate(decod_image[:, i*32:i*32+32], glyph_image, cv2.TM_SQDIFF_NORMED)
        mn, _, mnLoc, _ = cv2.minMaxLoc(result)
        MPx, MPy = mnLoc
        n = round(MPx / 32)
        glyphs += '0123456789abcdef'[n]
    return glyphs

glyph_image = cv2.imread('i/glyph_image.png', cv2.IMREAD_GRAYSCALE)
decod_image = cv2.imread('i/20240329192924_1.jpg', cv2.IMREAD_GRAYSCALE)[1015:1047,11:395]
print(isGlyphs(glyph_image, decod_image)) # 10b8fc003906 ► NMS-Glyphs-Mono.ttf