# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScib(PythonPackage):
	"""Evaluating single-cell data integration methods"""
	
	homepage = "https://github.com/theislab/scib"
	pypi = "scib/scib-1.1.5-1-py3-none-any.whl" 

	version("1.0.0", sha256="c34bea741f4183e34a7e8811043a50bac76ead44569ac33f65d46ed42b06c77c", expand=False, url="https://files.pythonhosted.org/packages/10/9c/da43e1b07575cc7e885a0704e7e580d1603765fc633d8f5d8a9f5928c945/scib-1.0.0-1-py3-none-any.whl")
	version("1.0.1", sha256="e1240a017257dfcda3d3626f5fba7dcde4d3d34436ef59aa6c35cfe0966f7eb1", expand=False, url="https://files.pythonhosted.org/packages/7e/86/bfe1acff3a117e3ce4217302505770d8afdb22728519495f7d4f3205d509/scib-1.0.1-1-py3-none-any.whl")
	version("1.0.2", sha256="d7d0fa9052d1463a0af008bfc006e4fccdb5c79e6e7d044549079ddbe68510ac", expand=False, url="https://files.pythonhosted.org/packages/a6/d5/57dbee153548598cf31f7cc4c95b0b71bbe98dcaffa2f1972e9c908474db/scib-1.0.2-1-py3-none-any.whl")
	version("1.0.3", sha256="134ad2a840990137d5cacd55d9b4cdd7f5f208973a940440ec94013635cac04f", expand=False, url="https://files.pythonhosted.org/packages/a5/ec/483cbc44a07ed0605b508c50a4251c2fe5693f60ac91c767eac6b51acb73/scib-1.0.3-1-py3-none-any.whl")
	version("1.0.4", sha256="d41ff001e3a1ed0f949456719d8ee54b817f8052d2cabc79f3dba71c68bea33b", expand=False, url="https://files.pythonhosted.org/packages/7b/83/25b8c5a5f600009f451ebdf4e76bcd2fe1654ed8c7bd9a69de92ffe571e2/scib-1.0.4-1-py3-none-any.whl")
	version("1.0.5", sha256="73365271c72119723b03dc225964872d101e10207ba7dd7c2783f5b659e241dc", expand=False, url="https://files.pythonhosted.org/packages/09/ad/df06dd5f19753bd6cf1a1682f1523c70d60aeff42034515cd460152d9166/scib-1.0.5-1-py3-none-any.whl")
	version("1.1.1", sha256="76398573bcca6ab508c20df98dcf92f86e17d8f093dbe220f212c6704bae11e2", expand=False, url="https://files.pythonhosted.org/packages/7b/f0/72868b6eff9de4f7de44dc8f09b25210fc3e2a3ae4e65aa5dd0dd175a4b0/scib-1.1.1-1-py3-none-any.whl")
	version("1.1.2", sha256="cdf2dbc7af4d891da59be90ac1faaca92d336e12d9d00f96a453bb90eaef9522", expand=False, url="https://files.pythonhosted.org/packages/8b/5c/c8a02fa53581eba856bb3ae24fe5ea679aa217fe86d64c79404f0beb0795/scib-1.1.2-1-py3-none-any.whl")
	version("1.1.3", sha256="85f6a5491a9a1d05d6795e0053a2388a848225291c8ab4b42a428d625ae593a7", expand=False, url="https://files.pythonhosted.org/packages/d2/20/430d434fee94a64d477f1ff12c4041b294f39b668648a8ff18d9ef3db963/scib-1.1.3-1-py3-none-any.whl")
	version("1.1.4", sha256="63dfe0920d661c6b815fe7c1e18e36240586422ce266dfda13466a7e7b243157", expand=False, url="https://files.pythonhosted.org/packages/19/96/38c9b0607e9f13937d960201d5e021a7d8025e908f34838abc9732aaa3db/scib-1.1.4-1-py3-none-any.whl")
	version("1.1.5", sha256="e5aec8037bb001a5f1b920ea81bac5288758e6013b2f89f1fbc3dcbd1e6c4e47", expand=False, url="https://files.pythonhosted.org/packages/c5/f4/4a27b5bec99be3f24a0634761deba4cd336962c105b70888294762fb3bf0/scib-1.1.5-1-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-deprecated", type=("build", "run"))
	depends_on("py-llvmlite", type=("build", "run"))
	depends_on("py-igraph", type=("build", "run"))
	depends_on("py-pydot", type=("build", "run"))
	depends_on("py-umap-learn", type=("build", "run"))
	depends_on("py-leidenalg", type=("build", "run"))
	depends_on("py-scikit-misc", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-scanpy", type=("build", "run"))
	depends_on("py-numba", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))

# {'numpy(==1.18.1)': ['1.0.0'], 'pandas': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3'], 'seaborn': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'matplotlib': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'numba': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'scanpy(>=1.5)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], 'anndata(>=0.7.2)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], 'h5py(<3)': ['1.0.0'], 'rpy2(>=3)': ['1.0.0', '1.0.1', '1.0.4'], 'anndata2ri': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], 'scipy': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'scikit-learn': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'scikit-misc': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'louvain': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], 'umap-learn': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'pydot': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'python-igraph': ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'llvmlite': ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "bbknn(==1.3.9);extra=='bbknn'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], "desc(==2.0.3);extra=='desc'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], "build;extra=='dev'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "twine;extra=='dev'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "isort;extra=='dev'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "bump2version;extra=='dev'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "mnnpy(==0.1.9.5);extra=='mnn'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], "scanorama(==1.7.0);extra=='scanorama'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], "scgen(==1.1.5);extra=='scgen'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], "scvi(==0.6.7);extra=='scvi'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], "pytest;extra=='test'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "pytest-runner;extra=='test'": ['1.0.0', '1.0.1', '1.0.2'], "pytest-icdiff;extra=='test'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "trvae(==1.1.2);extra=='trvae'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], "trvaep(==0.1.0);extra=='trvaep'": ['1.0.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], 'numpy': ['1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'h5py': ['1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'rpy2(<=3.4.2,>=3)': ['1.0.2', '1.0.3'], 'deprecated': ['1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "sphinx;extra=='docs'": ['1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "sphinx-rtd-theme;extra=='docs'": ['1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "myst-parser;extra=='docs'": ['1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "sphinx-automodapi;extra=='docs'": ['1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "pre-commit;extra=='dev'": ['1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "pytest-cov;extra=='test'": ['1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "codecov;extra=='test'": ['1.0.3', '1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'leidenalg': ['1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], 'igraph': ['1.0.4'], "scgen(>=2.1.0);extra=='scgen'": ['1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], "scvi-tools(>=0.16.1);extra=='scvi'": ['1.0.4', '1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], 'louvain(>=0.8)': ['1.0.5', '1.1.1'], 'igraph(>=0.10)': ['1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], "harmony-pytorch;extra=='harmony'": ['1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "rpy2(>=3);extra=='rpy2'": ['1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4'], "anndata2ri;extra=='rpy2'": ['1.0.5', '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5'], "python-igraph;extra=='louvain'": ['1.1.2', '1.1.3', '1.1.4', '1.1.5'], "louvain(>=0.8);extra=='louvain'": ['1.1.2', '1.1.3', '1.1.4'], 'pandas(<2)': ['1.1.4'], 'pandas>=2': ['1.1.5'], 'scanpy>=1.5': ['1.1.5'], 'anndata>=0.7.2': ['1.1.5'], 'igraph>=0.10': ['1.1.5'], "bbknn==1.3.9;extra=='bbknn'": ['1.1.5'], "desc==2.0.3;extra=='desc'": ['1.1.5'], "louvain>=0.8;extra=='louvain'": ['1.1.5'], "mnnpy==0.1.9.5;extra=='mnn'": ['1.1.5'], "rpy2>=3;extra=='rpy2'": ['1.1.5'], "scanorama>=1.7.4;extra=='scanorama'": ['1.1.5'], "scgen>=2.1.0;extra=='scgen'": ['1.1.5'], "scvi-tools>=0.16;extra=='scvi'": ['1.1.5'], "trvae==1.1.2;extra=='trvae'": ['1.1.5'], "trvaep==0.1.0;extra=='trvaep'": ['1.1.5']}