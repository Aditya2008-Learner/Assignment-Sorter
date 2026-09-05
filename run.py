import os
import sys
import uvicorn

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)
    
    from src.c_core.build import build_c_library
    build_c_library()
    
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "127.0.0.1")
    
    print(f"============================================================")
    print(f"  Assignment Sorter & AI Study Assistant")
    print(f"  Web Interface running at: http://{host}:{port}")
    print(f"============================================================")
    
    uvicorn.run("src.backend.app:app", host=host, port=port, reload=True)
