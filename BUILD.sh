printf "If there is a ModuleNotFoundError error, please run 'pip install site'\n"
site_pkgs=$(python3 -c 'import site; print(site.getsitepackages()[1])')
printf "site-packages location: $site_pkgs\n"

eval "sudo cp ./catfact.py $site_pkgs/catfact.py"