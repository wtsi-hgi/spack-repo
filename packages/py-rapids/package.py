# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRapids(PythonPackage):
	"""REST APIs documented and sensible"""
	
	homepage = "https://github.com/sinoroc/rapids"
	pypi = "rapids/rapids-0.0.1-py3-none-any.whl" 

	version("0.0.0", sha256="6f9b301d12094959cff1b63dd1d4fea69dadb13f5ad33e628d18ee53d80ee7bb", expand=False, url="https://files.pythonhosted.org/packages/85/87/f1ea905420adb582a509da0363bdb9a3ae4145e25fbcbcd522d0fc359368/rapids-0.0.0-py3-none-any.whl")
	version("0.0.1", sha256="fd614eae1478bea845b357e03473d87e17665c38547ee774b22ddf0c1922c4e0", expand=False, url="https://files.pythonhosted.org/packages/e1/51/1c8cbc90cbf1778699d0f9be280c84fac8058dcfc1da20d9976489cbae69/rapids-0.0.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-pyyaml", type=("build", "run"))
	depends_on("py-pyramid", type=("build", "run"))
	depends_on("py-setuptools", type=("build", "run"))
	depends_on("py-venusian", type=("build", "run"))
	depends_on("py-zope-interface", type=("build", "run"))

# {'pyramid': ['0.0.0', '0.0.1'], 'PyYaml': ['0.0.0'], 'venusian': ['0.0.0', '0.0.1'], 'zope.interface': ['0.0.0', '0.0.1'], 'PyYAML': ['0.0.1'], 'setuptools': ['0.0.1']}