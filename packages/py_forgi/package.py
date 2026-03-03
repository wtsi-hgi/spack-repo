# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyForgi(PythonPackage):
	"""RNA Graph Library"""
	
	homepage = "http://www.tbi.univie.ac.at/~pkerp/forgi/"
	pypi = "forgi/forgi-2.2.3.tar.gz" 

	version("0.1", sha256="80b89855a29de2b6ecf442454a967f99d682c3eef0f0d5ba9ade8026b3e02e74")
	version("0.20", sha256="02bcc321224bd75b257a287a2d5e2ba35135d560ddee2ec1e1e2caa7f3a9b46b")
	version("1.0", sha256="d5f6c5bad4475c9a6820816e07d9c2bea6ee364c9f45ea6214cc55e18513e381", expand=False, url="https://files.pythonhosted.org/packages/e4/70/94d2e42b6a8f96fd38e57fe1d3cc05335ac2e7e3b6599223701321356e0e/forgi-1.0-py2.py3-none-any.whl")
	version("1.1", sha256="a13ed8456dad061d5c5f05609847f58aa713a49993e7923dceadb036dfb92f54", expand=False, url="https://files.pythonhosted.org/packages/86/f7/812cba6327ac40a33d986b7d698a6d2193e64e7dfcd570abc6b4f86aede5/forgi-1.1-py2.py3-none-any.whl")
	version("2.0.1", sha256="4f70a6a3fa8a2533f3526344ce055b3a1ccc93d200ce74a83266705870151094")
	version("2.0.2", sha256="8cbe0701363993a17bfe61297139ef68d7efb635cb475769482a05740de1643f")
	version("2.1.2", sha256="68b3e9666b5c411c7862b5f98ac833b872345343e2d139554493cca2acb5b558")
	version("2.2.1", sha256="fe41a62166e6d6f73fcc49f0b911d03256f80113a79e8cc7b6e76f38ee3bddab")
	version("2.2.2", sha256="bceeb39a45fad41e3b8dbc9267f72d00082d1d855361bdfc45938e9b4e263e66")
	version("2.2.3", sha256="c87a455b1bdf91f91c1462777eda32ce1343fb149b688a406df3d7cebcb779ea")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-cython", type=("build"))
	depends_on("py-logging-exceptions", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-networkx", type=("build", "run"))
	depends_on("py-appdirs", type=("build", "run"))
	depends_on("py-biopython", type=("build", "run"))
	depends_on("py-beautifulsoup4", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
