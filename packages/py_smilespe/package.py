# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySmilespe(PythonPackage):
	"""Tokenize SMILES with substructure units"""
	
	homepage = "https://github.com/XinhaoLi74/SmilesPE"
	pypi = "smilespe/SmilesPE-0.0.3-py3-none-any.whl" 

	version("0.0.1", sha256="4ef0522dd1b353258e90046ec0905ff56086282dc8f0d9318c007da7c34fbdd7", expand=False, url="https://files.pythonhosted.org/packages/83/29/32a3a7afc1b1768010fde2dab2ab4f0585fe8262948c388ea254b8b4ba09/SmilesPE-0.0.1-py3-none-any.whl")
	version("0.0.2", sha256="5763f7c30df1558a80911f9e349045159d76b3be6e01f881d53d99b5b879341c", expand=False, url="https://files.pythonhosted.org/packages/66/2e/e10ccf110fdbde53b66527c44014fb9a69bcb7f7460fbc06dbd9cb7c58ba/SmilesPE-0.0.2-py3-none-any.whl")
	version("0.0.3", sha256="9f74279daa14945859546fb2de11c208b5116927ce5fe03b3cf46bcba96f5e58", expand=False, url="https://files.pythonhosted.org/packages/6d/f9/273f54d9d4b42779926291c82a5b3ffea30cff2492ebbe4ce08dccdcc949/SmilesPE-0.0.3-py3-none-any.whl")

	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-gensim", type=("build", "run"))
	depends_on("py-fastprogress", type=("build", "run"))

# {'fastprogress': ['0.0.1', '0.0.2', '0.0.3'], 'gensim': ['0.0.3']}