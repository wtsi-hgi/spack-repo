# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPytzDeprecationShim(PythonPackage):
	"""Shims to make deprecation of pytz easier"""
	
	homepage = "https://github.com/pganssle/pytz-deprecation-shim"
	pypi = "pytz-deprecation-shim/pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl" 

	version("0.1.0", sha256="4b4adc9952240b638de66a0a4d040050fcb8b48112619e38bbd58ead83de5506", expand=False, url="https://files.pythonhosted.org/packages/d3/99/8e6c2e788d301eba74fb911f2531f03e8064f9dbcd149ebb53ddef81fd4a/pytz_deprecation_shim-0.1.0-py2.py3-none-any.whl")
	version("0.1.0.post0", sha256="8314c9692a636c8eb3bda879b9f119e350e93223ae83e70e80c31675a0fdc1a6", expand=False, url="https://files.pythonhosted.org/packages/eb/73/3eaab547ca809754e67e06871cff0fc962bafd4b604e15f31896a0f94431/pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@2.7,3.6:", type=("build", "run"))

# {'python-dateutil;python_version<"3.6"': ['0.1.0', '0.1.0.post0'], 'tzdata;python_version>="3.6"': ['0.1.0', '0.1.0.post0'], 'backports.zoneinfo;python_version>="3.6"andpython_version<"3.9"': ['0.1.0', '0.1.0.post0']}