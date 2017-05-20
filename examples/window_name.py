import webview
import threading
import time

"""
This example demonstrates the usage of the name parameter of pywebview windows.

This script creates three windows: one main window in Python and two child windows in JS.
Then we apply three different API methods to them, referring each window by its name.

Currently works only on Mac.
"""

def load_html():
    webview.load_html(
        """
        <h3>This is the main window</h3>
        <p>This window is going to get destroyed!</p>
        <script>
        child_1 = window.open('', 'child_1', 'left=600,width=400,height=300');
        child_1.document.write(
            '<h3>This is the first child window</h3>\\
             <p>The content of this window will change.</p>'
        );

        child_2 = window.open('', 'child_2', 'left=300,top=400,width=400,height=300');
        child_2.document.write(
            '<h3>This is the second child window</h3>\\
             <p>This window will become fullscreen...</p>'
         );
         </script>
         """,
         name='main_window'
     )

def modify_windows():
    time.sleep(5)
    print 'Destroying the main window...'
    webview.destroy_window('main_window')

    time.sleep(2)
    print 'Loading new HTML content into the first child window...'
    webview.load_html('<h3>New content!</h3>', name='child_1')

    time.sleep(2)
    print 'Making the second child window fullscreen...'
    webview.toggle_fullscreen('child_2')

if __name__ == '__main__':
    t1 = threading.Thread(target=load_html)
    t2 = threading.Thread(target=modify_windows)
    t1.start()
    t2.start()

    webview.create_window("Named windows", name="main_window", width=400, height=300)

