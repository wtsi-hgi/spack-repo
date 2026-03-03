# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyServerTiming(PythonPackage):
	"""None"""
	
	homepage = "None"
	pypi = "server_timing/server_timing-0.0.1-py3-none-any.whl" 

	version("0.0.1", sha256="549508918c3d54015ab8210f62c5bb63577120a3a7dfb1dc39eca82b63971657", expand=False, url="https://files.pythonhosted.org/packages/24/f5/69f2043a244829e88285fa3fa999304c062a0dea1338483c428c7a87ee4b/server_timing-0.0.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
