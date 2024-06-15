# build_files.sh
pip install -r requirements.txt
python3.12 manage.py collectstatic
#updated python3.9 to python3.12