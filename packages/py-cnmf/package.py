# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCnmf(PythonPackage):
	"""Consensus NMF for scRNA-Seq data"""
	
	homepage = "https://github.com/dylkot/cNMF"
	pypi = "cnmf/cnmf-1.6.0-py3-none-any.whl" 

	version("1.3.0", sha256="cfa712367419a0379976ce307b35240dff24516d52c8161b1605af2dc05c4ba9")
	version("1.3.1", sha256="d78f2e77042dab143395a4f3a1410d45e2d5203294e10903d0fc2e238635f403")
	version("1.3.2", sha256="7f9e30b01b6a4579534f42023fa174d3f6683bdf8aabbcdabbda06f265492722")
	version("1.3.4", sha256="f0c157da4dcfb38f9dbc1ba4e60c86bc3294aa8a6b17f5ba1df0f14a2556259e", expand=False, url="https://files.pythonhosted.org/packages/4d/cb/18258e4f876bf94a79ea955d7faa2d9e6676ce0ceebd7aec74a300fa7a58/cnmf-1.3.4-py3-none-any.whl")
	version("1.4.1", sha256="40f8f2b27fc48778a661b40bedd064b47405a94ce1997d0d5d20382fc8998fe5", expand=False, url="https://files.pythonhosted.org/packages/df/ac/adce5b41a5e295b75b220fb58618d9366257bc7730fb42455970e30581ea/cnmf-1.4.1-py3-none-any.whl")
	version("1.5.0", sha256="20e2b75b2a5a35c55a071c7f5038a2460f89830c2a9aec6a2f17fbc1fa70f17d", expand=False, url="https://files.pythonhosted.org/packages/68/c8/f7a3b64ce9b967d978a4ed5445b6cdfef183e6bfe3606aa1d66f8ba7f971/cnmf-1.5.0-py3-none-any.whl")
	version("1.5.1", sha256="86166ad46e6ee3ec18764f69d92ee731a64c319c4e4f7acfcda18233c6065272", expand=False, url="https://files.pythonhosted.org/packages/fb/ad/a75e8a919ccc17cc07d7088cd364cc10a8db036d0f9174fb2da9c9a9311d/cnmf-1.5.1-py3-none-any.whl")
	version("1.5.2", sha256="0d42cad4bb656f5372f3bfee49eeeb0b919809c50989aa91adde128cd898f261", expand=False, url="https://files.pythonhosted.org/packages/3c/e4/6c238f13e57423cfe87a7eb9d958044a3b6b2b563de814cf959f833263d0/cnmf-1.5.2-py3-none-any.whl")
	version("1.5.3", sha256="e5c366a020e2203baaf4b6976938f243fa574245965e36604b1576ae18451983", expand=False, url="https://files.pythonhosted.org/packages/f7/ca/22fc0b9cf2b175fcb74f869dccb9fc7c9306291a5a63db50c71dde2dab62/cnmf-1.5.3-py3-none-any.whl")
	version("1.5.4", sha256="e6c22085fad973f5d365813b18e03531ba66f570e5007cfff225bd760bb304b7", expand=False, url="https://files.pythonhosted.org/packages/26/5d/e8642c03e88b29cd41eb2a8efec67bf6f3e40f7052ef2b33fd0f94902099/cnmf-1.5.4-py3-none-any.whl")
	version("1.6.0", sha256="17c64fb3ce93f65ab944505fb31acf316b913ee908a2af8bb645646b21b30097", expand=False, url="https://files.pythonhosted.org/packages/6a/2b/efd293dc0eb13eb257086eaeb461333b172a8f875cd39698d1d897ccf035/cnmf-1.6.0-py3-none-any.whl")

	depends_on("py-pyyaml", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-palettable", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-fastcluster", type=("build", "run"))
	depends_on("py-numpy@:1.23", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-scanpy", type=("build", "run"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))

# {'scikit-learn(>=1.0)': ['1.3.4', '1.5.2'], 'scanpy': ['1.3.4', '1.4.1', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.6.0'], 'pandas': ['1.3.4', '1.4.1', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.6.0'], 'numpy': ['1.3.4', '1.4.1', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.6.0'], 'fastcluster': ['1.3.4', '1.4.1', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.6.0'], 'matplotlib': ['1.3.4', '1.4.1', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.6.0'], 'palettable': ['1.3.4', '1.4.1', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.6.0'], 'scipy': ['1.3.4', '1.4.1', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.6.0'], 'pyyaml': ['1.3.4', '1.4.1', '1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.6.0'], 'scikit-learn>=1.0': ['1.4.1', '1.5.0', '1.5.1', '1.5.3', '1.5.4', '1.6.0'], 'anndata>=0.9': ['1.5.0', '1.5.1', '1.5.3', '1.5.4', '1.6.0'], 'anndata(>=0.9)': ['1.5.2']}