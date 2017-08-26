import webview

"""
A sample PDF reader application by combining PDF.js & Pywebview.
"""

if __name__ == '__main__':
    webview.create_window("Pywebview + PDF.js Reader", "./web/viewer.html?file=", background_color="#404040")
