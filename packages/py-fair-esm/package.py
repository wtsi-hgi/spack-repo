# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFairEsm(PythonPackage):
	"""Evolutionary Scale Modeling (esm): Pretrained language models for proteins. From Facebook AI Research."""
	
	homepage = "https://github.com/facebookresearch/esm"
	pypi = "fair-esm/fair_esm-2.0.0-py3-none-any.whl" 

	version("0.1.0", sha256="9eea790410855367a4d8a1cab4175c57454fab1cb043b2c138e34231a1933cdf", expand=False, url="https://files.pythonhosted.org/packages/ec/cb/d883419e37091e3a892ce526eed2d68bc3f7699af7339605fe74752e1691/fair_esm-0.1.0-py3-none-any.whl")
	version("0.1.1", sha256="72712291124fa1582b8acc0991bf67664d76fd37bb2ebf940b5a602ec851e37d", expand=False, url="https://files.pythonhosted.org/packages/65/ba/9be537b8777881103f2ae0cbeeeaa0dc84625cb3ac2b2d9e6cafcf4244aa/fair_esm-0.1.1-py3-none-any.whl")
	version("0.2.0", sha256="ef9d6a1dbc5f72c35bbef915d55449e8286d7da2f12fdfe0b644372c6a69dc7c", expand=False, url="https://files.pythonhosted.org/packages/f7/2c/3e266873a3381fd3f5335ee619f74ffc371e54e3aa269fe01f6e726bf6fe/fair_esm-0.2.0-py3-none-any.whl")
	version("0.3.0", sha256="f1ceb2276d66a7f3bbc47e264cdb9954952350e6d8fb15d4757e0d619c8584e3", expand=False, url="https://files.pythonhosted.org/packages/07/8f/b6aa8cafbb4f0dfc15ddd560bb59587191e187039f72a04acb81f397ae1f/fair_esm-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="cc6d240eae033efad3b01c9252507a3bf951a0bfb3de4207f58111df81883bed", expand=False, url="https://files.pythonhosted.org/packages/b7/40/3e757e044a9283a9b80b872aab32246fb0e4d725a57a0ef6ab7b9ef5e1c9/fair_esm-0.3.1-py3-none-any.whl")
	version("0.4.0", sha256="7f46a2ec89526848359c5bbb7bbb4bae8ed30291337624016d55eb23ff44af32", expand=False, url="https://files.pythonhosted.org/packages/aa/df/6740cfefda229a68ac72a03f8aff35dbfb10b6742a8b8c76aeece8889430/fair_esm-0.4.0-py3-none-any.whl")
	version("0.4.2", sha256="3c185ce7a63cdcf7996f82680b17a43ab905b577db589481f688933f469246e5", expand=False, url="https://files.pythonhosted.org/packages/b5/3a/48c8b46f3a17c8a8ed8f9546c4f7b1ac617bb0cf2bf530b7d7f57ab9fa6e/fair_esm-0.4.2-py3-none-any.whl")
	version("0.5.0", sha256="b016548e1cedbc57494a0db7d91ac2bb568058e0528adebe9e6587697424967a", expand=False, url="https://files.pythonhosted.org/packages/b2/1b/2fee28e7d550779bb3bb53b2ebf8ee3dbe39a42ae8d05511f834b24ddd5a/fair_esm-0.5.0-py3-none-any.whl")
	version("1.0.0", sha256="a6e53c1bc1f1801e5199defc421d8d3359deb5fa26620539c132fee4ed793a00", expand=False, url="https://files.pythonhosted.org/packages/a2/8d/846f679764b7b55ff94d271f8be164ebc77a8fe62ce2570e9d31788a6c10/fair_esm-1.0.0-py3-none-any.whl")
	version("1.0.2", sha256="95405647ff37023d18bd5b032b8f5788e3c0d53b64f33af23b4ab0a11d405c83", expand=False, url="https://files.pythonhosted.org/packages/11/18/7367b52b53e5c0d16eae4a63f00782bdfe87db1111433a92808c7f86d5b5/fair_esm-1.0.2-1-py3-none-any.whl")
	version("1.0.3", sha256="68ee670bc66057a7e3ff3b1756a50c2be9eea3708ae4d608b1f9f5270b67576c", expand=False, url="https://files.pythonhosted.org/packages/fd/9d/5c7a30e36f94c843595d2086c8fca3f5ebdd2d1445fb76bfbc8298f6bb9b/fair_esm-1.0.3-py3-none-any.whl")
	version("2.0.0", sha256="7dcb58828a401155d1457d071a03800bd1a50331ddf24ac79ad1dd0f2ea682a2", expand=False, url="https://files.pythonhosted.org/packages/79/26/1cc82571f507b9dae3b36d4242764edc6e4ae9f3f81f44a6382c15fad565/fair_esm-2.0.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-torch", type=("build", "run"))

# {"biopython;extra=='esmfold'": ['2.0.0'], "deepspeed(==0.5.9);extra=='esmfold'": ['2.0.0'], "dm-tree;extra=='esmfold'": ['2.0.0'], "pytorch-lightning;extra=='esmfold'": ['2.0.0'], "omegaconf;extra=='esmfold'": ['2.0.0'], "ml-collections;extra=='esmfold'": ['2.0.0'], "einops;extra=='esmfold'": ['2.0.0'], "scipy;extra=='esmfold'": ['2.0.0']}