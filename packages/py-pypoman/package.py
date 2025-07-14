# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPypoman(PythonPackage):
	"""Python module for polyhedral geometry."""
	
	homepage = "https://github.com/stephane-caron/pypoman"
	pypi = "pypoman/pypoman-1.2.0-py3-none-any.whl" 

	version("0.5.0", sha256="7fe2cc6463b935be9dba1707fa489b626afe01acd5e84786c80a5ad823753608")
	version("0.5.1", sha256="6563260cfa88349c2f8e9def0b91533550e74f17b39503247fa75bece4e32dce")
	version("0.5.2", sha256="65236a77ada5fb80d88ec142b9e9539162522ba4068ff8e9f1245f85fb18b0df")
	version("0.5.3", sha256="5f1ddf2174d30d51ceb533645f54bdedccda10f935a5eef42346581b1bafd4dd")
	version("0.5.4", sha256="52a649f7f5cb44d74e47688d8c5e943ddab9bce9f04b6f0676305b78c0ac1c66")
	version("0.6.0", sha256="45eb7ceab3541d7d45fecf31a81eafe4645b2c13e4e3478600730070603b5a49", expand=False, url="https://files.pythonhosted.org/packages/b6/b6/0966aeecb34fcb7c864ed50c23bc88ba1265b3c6e3da2104cb95ed4997dd/pypoman-0.6.0-py3-none-any.whl")
	version("1.0.0", sha256="53602c6800839b39b33ccee60ef1afbbc475f70dfd5d0e2b736a15499804ab72", expand=False, url="https://files.pythonhosted.org/packages/9f/1f/41df88e28741e36aad74b53f5f11a27e2289ec74d3fc9899a99602debdb2/pypoman-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="8893d7dd7212a43c88c08cf3b11ca260f2e4e7d7d20f0183afb3645a91eeedc4", expand=False, url="https://files.pythonhosted.org/packages/f4/9f/dd2a2014e519f83a3f4616bcc1400ce34bba21fb497477ac5ef9a1249fb1/pypoman-1.1.0-py3-none-any.whl")
	version("1.1.1", sha256="e5808a9be56a2475ba0a1df476ad30ce6e6111c2c88e831e906a79e34d72e33f", expand=False, url="https://files.pythonhosted.org/packages/cc/5f/1ee409113acad698e208eb17c364737ed503731e2430903ce5beb785ac59/pypoman-1.1.1-py3-none-any.whl")
	version("1.2.0", sha256="7af008697e6a720f69f7501e7f072c3ab366fa2759aba983192c317283c4337e", expand=False, url="https://files.pythonhosted.org/packages/e5/8b/5dba19312eab895c4aff368228f1b0f25cd743bcbce5b274b4499f1b13d3/pypoman-1.2.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pycddlib", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-cvxopt", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))

# {'cvxopt': ['0.6.0', '1.0.0'], 'matplotlib': ['0.6.0', '1.0.0'], 'numpy': ['0.6.0', '1.0.0'], 'pycddlib': ['0.6.0', '1.0.0'], 'scipy': ['0.6.0', '1.0.0'], 'cvxopt>=1.2.6': ['1.1.0', '1.1.1', '1.2.0'], 'matplotlib>=3.3.4': ['1.1.0', '1.1.1', '1.2.0'], 'numpy>=1.15.4': ['1.1.0', '1.1.1', '1.2.0'], 'pycddlib>=2.1.4': ['1.1.0'], 'scipy>=1.7.0': ['1.1.0', '1.1.1', '1.2.0'], 'pyclipper>=1.3.0;extra=="all"': ['1.1.0', '1.1.1', '1.2.0'], 'qpsolvers>=3.3.1;extra=="all"': ['1.1.0', '1.1.1', '1.2.0'], 'pycddlib>=2.1.4,<3': ['1.1.1'], 'pycddlib>=3.0.0': ['1.2.0']}