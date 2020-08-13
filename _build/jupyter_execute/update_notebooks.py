from glob import glob
import nbformat as nbf

notebooks = glob("./content/**/*.ipynb", recursive=True)

kernelspec = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}

for intbk in notebooks:
    ntbk = nbf.read(intbk, nbf.NO_CONVERT)
    ntbk.metadata['kernelspec'] = kernelspec
    nbf.write(ntbk, intbk)

