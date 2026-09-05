import os
import sys
import ctypes
import math
import platform
import numpy as np
from PIL import Image

_lib = None
_lib_loaded = False

def _init_c_library():
    global _lib, _lib_loaded
    if _lib_loaded:
        return _lib
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    is_windows = platform.system() == "Windows"
    lib_name = "libstudyc.dll" if is_windows else "libstudyc.so"
    lib_path = os.path.join(current_dir, lib_name)
    
    if not os.path.exists(lib_path):
        from .build import build_c_library
        build_c_library()
        
    if os.path.exists(lib_path):
        try:
            _lib = ctypes.CDLL(lib_path)
            
            _lib.c_levenshtein.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            _lib.c_levenshtein.restype = ctypes.c_int
            
            _lib.c_fuzzy_similarity.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            _lib.c_fuzzy_similarity.restype = ctypes.c_double
            
            _lib.c_bm25_term_score.argtypes = [
                ctypes.c_int, ctypes.c_int, ctypes.c_double,
                ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double
            ]
            _lib.c_bm25_term_score.restype = ctypes.c_double
            
            _lib.c_batch_bm25_scores.argtypes = [
                ctypes.POINTER(ctypes.c_int),
                ctypes.POINTER(ctypes.c_int),
                ctypes.c_int,
                ctypes.c_double,
                ctypes.c_int,
                ctypes.c_int,
                ctypes.c_double,
                ctypes.c_double,
                ctypes.POINTER(ctypes.c_double)
            ]
            _lib.c_batch_bm25_scores.restype = None
            
            _lib.c_fnv1a_hash.argtypes = [ctypes.c_char_p]
            _lib.c_fnv1a_hash.restype = ctypes.c_ulonglong
            
            _lib.c_rgb_to_grayscale.argtypes = [
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.c_int, ctypes.c_int
            ]
            _lib.c_rgb_to_grayscale.restype = None
            
            _lib.c_otsu_threshold.argtypes = [
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.c_int, ctypes.c_int
            ]
            _lib.c_otsu_threshold.restype = ctypes.c_int
            
            _lib.c_binarize_otsu.argtypes = [
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.c_int, ctypes.c_int
            ]
            _lib.c_binarize_otsu.restype = None
            
            _lib.c_enhance_contrast.argtypes = [
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.c_int, ctypes.c_int
            ]
            _lib.c_enhance_contrast.restype = None
            
            _lib.c_median_filter_3x3.argtypes = [
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.POINTER(ctypes.c_ubyte),
                ctypes.c_int, ctypes.c_int
            ]
            _lib.c_median_filter_3x3.restype = None
            
            _lib_loaded = True
            return _lib
        except Exception as e:
            print(f"Warning: Failed to load C library at {lib_path}: {e}", file=sys.stderr)
            _lib_loaded = False
            return None
    return None

_init_c_library()

def fast_levenshtein(s1: str, s2: str) -> int:
    lib = _init_c_library()
    if lib:
        b1 = s1.encode('utf-8', errors='ignore')
        b2 = s2.encode('utf-8', errors='ignore')
        return lib.c_levenshtein(b1, b2)
    
    s1, s2 = s1.lower(), s2.lower()
    if len(s1) < len(s2):
        return fast_levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def fast_fuzzy_similarity(s1: str, s2: str) -> float:
    lib = _init_c_library()
    if lib:
        b1 = s1.encode('utf-8', errors='ignore')
        b2 = s2.encode('utf-8', errors='ignore')
        return float(lib.c_fuzzy_similarity(b1, b2))
    
    if not s1 and not s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    dist = fast_levenshtein(s1, s2)
    max_len = max(len(s1), len(s2))
    return 1.0 - (dist / max_len)

def fast_bm25_term_score(tf: int, doc_len: int, avg_doc_len: float, doc_count: int, df: int, k1: float = 1.5, b: float = 0.75) -> float:
    lib = _init_c_library()
    if lib:
        return float(lib.c_bm25_term_score(tf, doc_len, avg_doc_len, doc_count, df, k1, b))
    
    if tf <= 0 or df <= 0 or doc_count <= 0 or avg_doc_len <= 0:
        return 0.0
    idf = math.log(1.0 + (doc_count - df + 0.5) / (df + 0.5))
    if idf < 0:
        idf = 0.0
    len_norm = 1.0 - b + b * (doc_len / avg_doc_len)
    tf_norm = (tf * (k1 + 1.0)) / (tf + k1 * len_norm)
    return idf * tf_norm

def fast_batch_bm25(tfs: list[int], doc_lens: list[int], avg_doc_len: float, total_docs: int, df: int, k1: float = 1.5, b: float = 0.75) -> list[float]:
    num_docs = len(tfs)
    if num_docs == 0:
        return []
    
    lib = _init_c_library()
    if lib:
        tfs_arr = (ctypes.c_int * num_docs)(*tfs)
        doc_lens_arr = (ctypes.c_int * num_docs)(*doc_lens)
        out_scores = (ctypes.c_double * num_docs)()
        lib.c_batch_bm25_scores(
            tfs_arr, doc_lens_arr, num_docs, avg_doc_len, total_docs, df, k1, b, out_scores
        )
        return [float(x) for x in out_scores]
    
    return [fast_bm25_term_score(tfs[i], doc_lens[i], avg_doc_len, total_docs, df, k1, b) for i in range(num_docs)]

def fast_hash_string(s: str) -> int:
    lib = _init_c_library()
    if lib:
        return int(lib.c_fnv1a_hash(s.encode('utf-8', errors='ignore')))
    
    hash_val = 14695981039346656037
    for byte in s.lower().encode('utf-8', errors='ignore'):
        hash_val ^= byte
        hash_val = (hash_val * 1099511628211) & 0xFFFFFFFFFFFFFFFF
    return hash_val

def preprocess_image_for_ocr(image: Image.Image) -> Image.Image:
    lib = _init_c_library()
    img_rgb = image.convert("RGB")
    width, height = img_rgb.size
    
    np_rgb = np.array(img_rgb, dtype=np.uint8)
    if lib:
        try:
            gray_buf = np.empty((height, width), dtype=np.uint8)
            filtered_buf = np.empty((height, width), dtype=np.uint8)
            bin_buf = np.empty((height, width), dtype=np.uint8)
            
            rgb_ptr = np_rgb.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
            gray_ptr = gray_buf.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
            filtered_ptr = filtered_buf.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
            bin_ptr = bin_buf.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
            
            lib.c_rgb_to_grayscale(rgb_ptr, gray_ptr, width, height)
            lib.c_enhance_contrast(gray_ptr, width, height)
            lib.c_median_filter_3x3(gray_ptr, filtered_ptr, width, height)
            lib.c_binarize_otsu(filtered_ptr, bin_ptr, width, height)
            
            return Image.fromarray(bin_buf, mode="L")
        except Exception as e:
            print(f"C image preprocessing fallback: {e}", file=sys.stderr)
            
    img_gray = img_rgb.convert("L")
    return img_gray
