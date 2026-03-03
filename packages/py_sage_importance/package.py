# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySageImportance(PythonPackage):
	"""For calculating global feature importance using Shapley values."""
	
	homepage = "https://github.com/iancovert/sage/"
	pypi = "sage-importance/sage_importance-0.0.6-py3-none-any.whl" 

	version("0.0.1", sha256="c91dec673554d3616051a41d90de92de820e8164f8c0af51fe70916388c06a8f", expand=False, url="https://files.pythonhosted.org/packages/36/00/0b3cdea104433fa56abc7c32c7b61ad94f7e6a251d4882feffb9b0873864/sage_importance-0.0.1-py3-none-any.whl")
	version("0.0.2", sha256="e95a024bb9857b333c44d4730ca2561545f43926a2816c8fb41df6c8a4eb1da3", expand=False, url="https://files.pythonhosted.org/packages/d6/15/b0a67d0a013793ec26a1b6b82814a7c99bc7b2e6ffda105f1621e5452a44/sage_importance-0.0.2-py3-none-any.whl")
	version("0.0.3", sha256="32a7138c9fbb31b54747c5cbcbc6c82c02bec8fde459563978ec1e29c51446ab", expand=False, url="https://files.pythonhosted.org/packages/00/94/44c69a764949b970639d0d483dbd2728fbc2e4ad831e9a65da4efad0b0ae/sage_importance-0.0.3-py3-none-any.whl")
	version("0.0.4", sha256="c32f7ba2534b2cb507d684960b6afbe05dbe1f1ef4713925d88a4d9ce1239bd2", expand=False, url="https://files.pythonhosted.org/packages/99/cc/207b9d3c5192841700ff5490f9794e05575fd993dfb8f9960910a6326d98/sage_importance-0.0.4-py3-none-any.whl")
	version("0.0.5", sha256="796810840bfcb6e57d4043da0c0d387af811c3ad5dcbd57f5cf53ca4b137a548", expand=False, url="https://files.pythonhosted.org/packages/17/16/2bc465921f238baa5284a4ec2208717cfee2380607e6472a2a73cd0686bf/sage_importance-0.0.5-py3-none-any.whl")
	version("0.0.6", sha256="db94171ce7ac43176ad5cdced536f4fe157d14ec3c0d9b044bdab24e6c2fb3a5", expand=False, url="https://files.pythonhosted.org/packages/92/73/fc28f24d44ce0c07b844397de8bd2ed4b6f8d183ae56cae13371e0909a2a/sage_importance-0.0.6-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-joblib", type=("build", "run"))


# {'numpy': ['0.0.1', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.0.6'], 'matplotlib': ['0.0.1', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.0.6'], 'tqdm': ['0.0.1', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.0.6'], 'scipy': ['0.0.4', '0.0.5', '0.0.6'], 'joblib': ['0.0.5', '0.0.6'], "build;extra=='dev'": ['0.0.6'], "pre-commit;extra=='dev'": ['0.0.6'], "catboost;extra=='notebook'": ['0.0.6'], "ipykernel;extra=='notebook'": ['0.0.6'], "gender-guesser;extra=='notebook'": ['0.0.6'], "pandas;extra=='notebook'": ['0.0.6'], "tensorflow;extra=='notebook'": ['0.0.6'], "torch;extra=='notebook'": ['0.0.6'], "torchvision;extra=='notebook'": ['0.0.6'], "scikit-learn;extra=='notebook'": ['0.0.6'], "xgboost;extra=='notebook'": ['0.0.6']}