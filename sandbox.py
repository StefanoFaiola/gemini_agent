import subprocess

sub = subprocess.run(["python", "test_write_file.py"], capture_output=True, text=True )

print(type(sub))
print(sub.returncode)
print(sub.stdout)