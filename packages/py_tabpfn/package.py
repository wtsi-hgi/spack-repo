# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTabpfn(PythonPackage):
	"""TabPFN: Foundation model for tabular data"""
	
	homepage = "http://priorlabs.ai"
	pypi = "tabpfn/tabpfn-2.0.9-py3-none-any.whl" 

	version("0.1.11", sha256="d7699467049cf6e3950121777a5ee6aa625cb9066447a7888f8ebf8937d3858a", expand=False, url="https://files.pythonhosted.org/packages/0e/e9/b95d9970c0a55c8bc41bb8b653c21b7cc034506cca4d6f6929d97f04f41e/tabpfn-0.1.11-py3-none-any.whl")
	version("2.0.0", sha256="ff0284d4492eff7ebe1af2ab6522bb2598893531950623e25ab767f63a227b97", expand=False, url="https://files.pythonhosted.org/packages/ac/24/211ec39c89722da6bb5676d0c0d3b6c6968ae94c317b8ba49d1afa39c0b1/tabpfn-2.0.0-py3-none-any.whl")
	version("2.0.1", sha256="f7ff09908b077ee32408c477674f7e86592103e9279cb85f9d40f27b7fd55a06", expand=False, url="https://files.pythonhosted.org/packages/25/e1/091a782ec7c8b7112afa905c77cec2b201d50d4ce61fe4aba76743b6ef8e/tabpfn-2.0.1-py3-none-any.whl")
	version("2.0.2", sha256="ebd86abfc9915042ef03646b995cc14551e306bca78aae5274c058cdddae795e", expand=False, url="https://files.pythonhosted.org/packages/b2/78/bfa972c18c73a513c64a45ea0278e034fec1edbdb1ee678bb14289e678ca/tabpfn-2.0.2-py3-none-any.whl")
	version("2.0.3", sha256="5faccd9aaea919e8a16aa1e939f3ac4909581779f64f6cadf8b956b16daebac4", expand=False, url="https://files.pythonhosted.org/packages/4e/64/cb1a07182aba215648cedb03dff0e23d1bb1ab02f696a10aaa5a4759e311/tabpfn-2.0.3-py3-none-any.whl")
	version("2.0.4", sha256="b5051533bcca83274dec833a72234f5b7aec6b9052b216829c96dd0a8554a9a0", expand=False, url="https://files.pythonhosted.org/packages/a6/93/b8b2f298b3cd4462c49db6718a0d0a3221c49c1af8d7c2354193caae746b/tabpfn-2.0.4-py3-none-any.whl")
	version("2.0.5", sha256="cf2b7730af25c8c84a1a9ce46ee60f6f71721d8099626b87b60c55c934330351", expand=False, url="https://files.pythonhosted.org/packages/0c/e2/a9db0978c79f1b2b5719f5a0df1714c6814881440321d4f48023ce42b2a5/tabpfn-2.0.5-py3-none-any.whl")
	version("2.0.6", sha256="30ddf989f9c4dd0e1af5d5c1ca7bc4412c0e6425c8c2ca4f68eaf4e46429b535", expand=False, url="https://files.pythonhosted.org/packages/7d/3c/edb9796519328e26d4ed11aa21e4d1b04783f598e161cdad2fb2d9792c46/tabpfn-2.0.6-py3-none-any.whl")
	version("2.0.7", sha256="64fdd63732f2f77c81dfde0d32bd88b29553356a614823e89bb52c34fd7078d1", expand=False, url="https://files.pythonhosted.org/packages/90/d8/c67878fbee1454cf807cb16821fac5e7cba6c5a3b0de8b9587198a175c19/tabpfn-2.0.7-py3-none-any.whl")
	version("2.0.8", sha256="b653ddca8119f91966f42da952b6f85cef29761f37a068b3fa87f8ce2b7c6939", expand=False, url="https://files.pythonhosted.org/packages/a6/40/6bab1f108d4c7eb2c4bd319abb2995e3ad1c31a353e94df23beb4fa36f07/tabpfn-2.0.8-py3-none-any.whl")
	version("2.0.9", sha256="04e3bb989e9328d510ea4fccb6c6a36c8269630685d460af4df5eb268206bf21", expand=False, url="https://files.pythonhosted.org/packages/35/f8/b0e7ff83484acfbe670b2f56c28c6bcf09ae84284e624cd45755a8b7073c/tabpfn-2.0.9-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-torch", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-typing-extensions", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-einops", type=("build", "run"))
	depends_on("py-huggingface-hub", type=("build", "run"))

# {'numpy>=1.21.2': ['0.1.11'], 'pyyaml>=5.4.1': ['0.1.11'], 'requests>=2.23.0': ['0.1.11'], 'scikit-learn>=0.24.2': ['0.1.11'], 'torch>=1.9.0': ['0.1.11'], "auto-sklearn>=0.14.5;extra=='full'": ['0.1.11'], "catboost>=0.26.1;extra=='full'": ['0.1.11'], "configspace>=0.4.21;extra=='full'": ['0.1.11'], "gpytorch>=1.5.0;extra=='full'": ['0.1.11'], "hyperopt>=0.2.5;extra=='full'": ['0.1.11'], "openml>=0.12.2;extra=='full'": ['0.1.11'], "seaborn==0.11;extra=='full'": ['0.1.11'], "tqdm>=4.62.1;extra=='full'": ['0.1.11'], "xgboost>=1.4.0;extra=='full'": ['0.1.11'], 'torch>=2.1': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'scikit-learn>=1': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'typing_extensions': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'scipy': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'pandas': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'einops': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'huggingface-hub': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'pre-commit;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'ruff;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mypy;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'pytest;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mkdocs;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mkdocs-material;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mkdocs-autorefs;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mkdocs-gen-files;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mkdocs-literate-nav;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mkdocs-glightbox;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mkdocstrings[python];extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'markdown-exec[ansi];extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'mike;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'black;extra=="dev"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'torch<3,>=2.1': ['2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'scikit-learn<1.7,>=1.2.0': ['2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'typing_extensions>=4.4.0': ['2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'scipy<2,>=1.7.3': ['2.0.4', '2.0.5', '2.0.6'], 'pandas<3,>=1.4.0': ['2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'einops<0.9,>=0.2.0': ['2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'huggingface-hub<1,>=0.0.1': ['2.0.4', '2.0.5', '2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'onnx;extra=="dev"': ['2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'psutil;extra=="dev"': ['2.0.6', '2.0.7', '2.0.8', '2.0.9'], 'scipy<2,>=1.11.1': ['2.0.7', '2.0.8', '2.0.9']}