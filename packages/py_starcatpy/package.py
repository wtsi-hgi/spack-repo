# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyStarcatpy(PythonPackage):
	"""Implements *CellAnnotator (aka *CAT/starCAT), annotating scRNA-Seq with predefined gene expression programs"""
	
	homepage = "https://github.com/immunogenomics/starCAT"
	pypi = "starcatpy/starcatpy-1.0.9-py3-none-any.whl" 

	version("1.0", sha256="dbe9c2670df5725279f6515cc84eec6eaef48025daf770e3960fe3082ca59c41", expand=False, url="https://files.pythonhosted.org/packages/02/f3/2a7abc3d78768fcf3bb1f91be79dad438b453e3fb319041229e1171d3c20/starcatpy-1.0-py3-none-any.whl")
	version("1.0.1", sha256="e9fcf7313e514f33c04619f9591739e54c2cb6a32a001234749f720face5f63c", expand=False, url="https://files.pythonhosted.org/packages/cd/a3/ae8a01445a26399be8acafecaee5373fc593ac4e445b3e2e561d93baf292/starcatpy-1.0.1-py3-none-any.whl")
	version("1.0.2", sha256="9496ce82279b202458997def9c1c37e3d3320009dff50b4800075c5c4d118b07", expand=False, url="https://files.pythonhosted.org/packages/be/35/feefef37be3c5dbb7745cea40388e37dbde5a72a02b6194b7aaa7aed99e3/starcatpy-1.0.2-py3-none-any.whl")
	version("1.0.3", sha256="0ac1cf7193bcc00ac3d11b70e49b8184c456d25fd29317404cd23b2e7dc3c670", expand=False, url="https://files.pythonhosted.org/packages/61/ba/f515fd96b8597037813f1c342afda3e4504120a15135ccfb4f274a8b810f/starcatpy-1.0.3-py3-none-any.whl")
	version("1.0.4", sha256="282de5b6358d88093648730a164032547f7db36a748d7beaebf4f4e258cbf209", expand=False, url="https://files.pythonhosted.org/packages/9d/0f/692add40825039ee9bf32d4fe6a998bbb021c75724c7ab12a8b0ec02360c/starcatpy-1.0.4-py3-none-any.whl")
	version("1.0.5", sha256="a113463f2dd5ee964a566d9b8d61cf6976fb0fe631e0b815dd19b71209a7a386", expand=False, url="https://files.pythonhosted.org/packages/08/05/a6a2a463c0a6cd6680c55170179467f17eb38275caddad43add9784d4f2d/starcatpy-1.0.5-py3-none-any.whl")
	version("1.0.6", sha256="083c075fc31d3f6dfec74fac4f745b695dcff7c16423d79a77a9f3f19b1723c6", expand=False, url="https://files.pythonhosted.org/packages/b6/d4/eafbfd1cbdfc3a5bc53b8bae2bbeee0669ace599552f736a4a2334ba86e0/starcatpy-1.0.6-py3-none-any.whl")
	version("1.0.7", sha256="8183bf7d35b8799493b2a10810b346c28cdc753f94b8d3a10b69d995ca16f0f8", expand=False, url="https://files.pythonhosted.org/packages/49/af/6ded9ecfd2cde52899b089b3657e14c22fefc7ebfa7a73cb4f911877de83/starcatpy-1.0.7-py3-none-any.whl")
	version("1.0.8", sha256="cc2479514046fd56eff901459389cfac3e2a58b12bbf1fdbd4b9b4225ba423c3", expand=False, url="https://files.pythonhosted.org/packages/58/56/81e23f14936c95771d7fdeb2d9568ad98f51624343c627ee25d78f2fb55f/starcatpy-1.0.8-py3-none-any.whl")
	version("1.0.9", sha256="0183e9cbde3ec577da7436d97811a9616adb1bbab0485de860ae3b132f789b8f", expand=False, url="https://files.pythonhosted.org/packages/94/ee/be9b5446c74a4f26be5cbd61085e264bdb6f00dc7c4ef1c364a7743f7b56/starcatpy-1.0.9-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pyyaml", type=("build", "run"))
	depends_on("py-requests", type=("build", "run"))
	depends_on("py-cnmf", type=("build", "run"))
	depends_on("py-fastcluster", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-palettable", type=("build", "run"))
	depends_on("py-scanpy", type=("build", "run"))

# {'scikit-learn(>=1.0)': ['1.0', '1.0.1'], 'scanpy': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5'], 'pandas': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9'], 'numpy': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9'], 'fastcluster': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], 'matplotlib': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], 'palettable': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], 'scipy': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9'], 'pyyaml': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9'], 'cnmf': ['1.0', '1.0.1', '1.0.2', '1.0.3', '1.0.4'], 'scikit-learn>=1.0': ['1.0.2', '1.0.3', '1.0.4', '1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9'], 'requests': ['1.0.5', '1.0.6', '1.0.7', '1.0.8', '1.0.9'], 'anndata': ['1.0.6', '1.0.7', '1.0.8', '1.0.9']}