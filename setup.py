from cx_Freeze import setup, Executable

setup(name = 'uwealth',
    version='1.0',
    description='Uwealth Parser',
    executables = [Executable("main.py")]
    )
