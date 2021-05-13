mkdir config
fsutil file createnew config\server.yaml 0  

python -m venv .\venv
.\venv\Scripts\activate.bat

python -m pip install -e .