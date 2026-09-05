#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT void c_rgb_to_grayscale(const unsigned char *rgb, unsigned char *gray, int width, int height) {
    if (!rgb || !gray || width <= 0 || height <= 0) return;
    int total_pixels = width * height;
    for (int i = 0; i < total_pixels; i++) {
        int r = rgb[i * 3 + 0];
        int g = rgb[i * 3 + 1];
        int b = rgb[i * 3 + 2];
        gray[i] = (unsigned char)((r * 299 + g * 587 + b * 114) / 1000);
    }
}

EXPORT void c_rgba_to_grayscale(const unsigned char *rgba, unsigned char *gray, int width, int height) {
    if (!rgba || !gray || width <= 0 || height <= 0) return;
    int total_pixels = width * height;
    for (int i = 0; i < total_pixels; i++) {
        int r = rgba[i * 4 + 0];
        int g = rgba[i * 4 + 1];
        int b = rgba[i * 4 + 2];
        gray[i] = (unsigned char)((r * 299 + g * 587 + b * 114) / 1000);
    }
}

EXPORT int c_otsu_threshold(const unsigned char *gray, int width, int height) {
    if (!gray || width <= 0 || height <= 0) return 128;
    int total_pixels = width * height;
    int hist[256] = {0};

    for (int i = 0; i < total_pixels; i++) {
        hist[gray[i]]++;
    }

    double sum = 0.0;
    for (int i = 0; i < 256; i++) {
        sum += (double)(i * hist[i]);
    }

    double sumB = 0.0;
    int wB = 0;
    int wF = 0;
    double varMax = 0.0;
    int threshold = 128;

    for (int t = 0; t < 256; t++) {
        wB += hist[t];
        if (wB == 0) continue;
        wF = total_pixels - wB;
        if (wF == 0) break;

        sumB += (double)(t * hist[t]);
        double mB = sumB / (double)wB;
        double mF = (sum - sumB) / (double)wF;

        double varBetween = (double)wB * (double)wF * (mB - mF) * (mB - mF);
        if (varBetween > varMax) {
            varMax = varBetween;
            threshold = t;
        }
    }
    return threshold;
}

EXPORT void c_binarize_otsu(const unsigned char *gray, unsigned char *bin_out, int width, int height) {
    if (!gray || !bin_out || width <= 0 || height <= 0) return;
    int threshold = c_otsu_threshold(gray, width, height);
    int total_pixels = width * height;
    for (int i = 0; i < total_pixels; i++) {
        bin_out[i] = (gray[i] >= threshold) ? 255 : 0;
    }
}

EXPORT void c_enhance_contrast(unsigned char *gray, int width, int height) {
    if (!gray || width <= 0 || height <= 0) return;
    int total_pixels = width * height;
    unsigned char min_val = 255;
    unsigned char max_val = 0;

    for (int i = 0; i < total_pixels; i++) {
        if (gray[i] < min_val) min_val = gray[i];
        if (gray[i] > max_val) max_val = gray[i];
    }

    if (max_val <= min_val) return;

    double scale = 255.0 / (double)(max_val - min_val);
    for (int i = 0; i < total_pixels; i++) {
        int val = (int)(((double)(gray[i] - min_val)) * scale);
        if (val < 0) val = 0;
        if (val > 255) val = 255;
        gray[i] = (unsigned char)val;
    }
}

EXPORT void c_median_filter_3x3(const unsigned char *src, unsigned char *dst, int width, int height) {
    if (!src || !dst || width < 3 || height < 3) {
        if (src && dst && width > 0 && height > 0) {
            memcpy(dst, src, width * height);
        }
        return;
    }

    memcpy(dst, src, width * height);

    for (int y = 1; y < height - 1; y++) {
        for (int x = 1; x < width - 1; x++) {
            unsigned char window[9];
            int idx = 0;
            for (int dy = -1; dy <= 1; dy++) {
                for (int dx = -1; dx <= 1; dx++) {
                    window[idx++] = src[(y + dy) * width + (x + dx)];
                }
            }
            for (int i = 0; i < 5; i++) {
                for (int j = i + 1; j < 9; j++) {
                    if (window[i] > window[j]) {
                        unsigned char temp = window[i];
                        window[i] = window[j];
                        window[j] = temp;
                    }
                }
            }
            dst[y * width + x] = window[4];
        }
    }
}
