import sys
from jupyter_book.cli.main import main

if __name__ == "__main__":
    sys.argv = ["jupyter-book", "build", "."]
    try:
        main()
    except SystemExit as e:
        print(f"Exited with code: {e.code}")
    except Exception as e:
        print(f"Error: {e}")
