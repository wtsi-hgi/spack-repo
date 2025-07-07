# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMvtcr(PythonPackage):
	"""mvTCR: A multimodal generative model to learn a unified representation across TCR sequences and scRNAseq data for joint analysis of single-cell immune profiling data"""
	
	homepage = "https://github.com/SchubertLab/mvTCR"
	pypi = "mvtcr/mvtcr-0.2.1.2-py2.py3-none-any.whl" 

	version("0.1.0", sha256="53878d3ca18c523eb6be27d366edb1015e313082f387ba92fb17696721c66af4")
	version("0.1.1", sha256="d8209608006098952b78c799461f7e193c64fd6ca8bce4f4fe2989a53b2efd90")
	version("0.1.2", sha256="47cab284e707d66179ccaf0eaf3db9155dacac7826006c49ec1dd996516e8243", expand=False, url="https://files.pythonhosted.org/packages/85/d9/7187c9e613213b6304cb671da516ac03a54bed4c09c2c22957ef298d08b8/mvtcr-0.1.2-py2.py3-none-any.whl")
	version("0.1.3", sha256="6ae6e313566c30038049a187cbffbd0368706641d08ac0bfd0f4c2b54cd10502", expand=False, url="https://files.pythonhosted.org/packages/4a/17/16bfa98d3b3e21598db510d6a1533097a1dbf7b48ba02d7681e028da806a/mvtcr-0.1.3-py2.py3-none-any.whl")
	version("0.2.0", sha256="1929668294ed63e76ebcfa2c93d4a4bc8871814e0e82026ef7021885ab63ce79", expand=False, url="https://files.pythonhosted.org/packages/99/a2/4b91e1b30ae8911c49cbc1d1d16dcdb3b3fd77d6f418c0a29f9e259606ae/mvtcr-0.2.0-py2.py3-none-any.whl")
	version("0.2.1", sha256="505bdc70396778b014211db84d8ba7733482701abc22339e2410f5d567707b18", expand=False, url="https://files.pythonhosted.org/packages/01/0e/5056f40cb55865beff34992281597d1cd04d1b67f802a1ba02e2fb3ab800/mvtcr-0.2.1-py2.py3-none-any.whl")
	version("0.2.1.1", sha256="66d1a9a7c600015a451a6847ca62e6704c808a9c610175a8ed150950351c1d11", expand=False, url="https://files.pythonhosted.org/packages/5e/88/0eccc98eea403d6cad95aeedd8c5f3a1f274f0f4b40cb7ee42e9f0ce7178/mvtcr-0.2.1.1-py2.py3-none-any.whl")
	version("0.2.1.2", sha256="79ec7b9488605012fa28a74a90da93113f4bbbcff3c404cd2eae1db11e775f9e", expand=False, url="https://files.pythonhosted.org/packages/ab/65/3eb28da0e52d1351a14544f7c3b812315ac506a946b179c1558eb5eaed68/mvtcr-0.2.1.2-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-comet-ml", type=("build", "run"))
	depends_on("py-leidenalg", type=("build", "run"))
	depends_on("py-muon", type=("build", "run"))
	depends_on("py-numba", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-optuna", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-scanpy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-scirpy", type=("build", "run"))
	depends_on("py-scrublet", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-umap-learn", type=("build", "run"))

# {'scanpy==1.7.0\r': ['0.1.2', '0.1.3'], 'scirpy>=0.7\r': ['0.1.2', '0.1.3'], 'numba==0.52.0\r': ['0.1.2', '0.1.3'], 'pandas==1.2.3\r': ['0.1.2', '0.1.3'], 'anndata==0.8.0\r': ['0.1.2', '0.1.3'], 'leidenalg==0.8.4\r': ['0.1.2', '0.1.3'], 'comet-ml\r': ['0.1.2', '0.1.3'], 'numpy==1.20.3\r': ['0.1.2', '0.1.3'], 'scikit-learn==0.24.1\r': ['0.1.2', '0.1.3'], 'scrublet==0.2.3\r': ['0.1.2', '0.1.3', '0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'tqdm\r': ['0.1.2', '0.1.3'], 'optuna==2.10.1\r': ['0.1.2', '0.1.3'], 'umap-learn==0.5.1\r': ['0.1.2', '0.1.3'], 'matplotlib==3.6.3\r': ['0.1.2', '0.1.3'], 'sqlalchemy==1.4.26\r': ['0.1.2', '0.1.3'], 'torch>=1.8.0\r': ['0.1.2'], 'dunamai==1.18.1\r': ['0.1.3'], 'anndata==0.10.3\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'comet-ml==3.35.5\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'leidenalg==0.10.1\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'muon==0.1.5\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'numba==0.58.1\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'numpy==1.26.1\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'optuna==3.4.0\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'pandas==2.1.1\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'scanpy==1.9.6\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'scikit-learn==1.3.2\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'scirpy==0.13.1\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'tqdm==4.66.1\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2'], 'umap-learn==0.5.4\r': ['0.2.0', '0.2.1', '0.2.1.1', '0.2.1.2']}