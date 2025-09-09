# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNorns(PythonPackage):
	"""Simple yaml-based config module"""
	
	homepage = "https://github.com/simonvh/norns"
	pypi = "norns/norns-0.1.6.tar.gz" 

	version("0.1.0", sha256="50cf9ac8b4896ee66d33dffcbb207a54b442d7fae73b89916097dba515db31bb")
	version("0.1.1", sha256="a23b3fa91c9a16caa903238d31e4fe2df04c4ca0cf0b9378de244f390e12bcb7")
	version("0.1.2", sha256="341bdf9ed858da0e12ca4d269e303e1f0ba08b54660588c324ffcaa9aa0de6d0")
	version("0.1.4", sha256="4c91543c6bd8855cdd8bb2ba3c971df08896a1bed206d4c7328227e58d7b2404")
	version("0.1.5", sha256="b713a7625ca88840b62bd704012b0ab50755a728eb47778324c386b8da2ed8ce")
	version("0.1.6", sha256="1f3c6ccbe79b2cb3076f66a352cd76462593adbabe9ebb262f879a9d0a6634e4")

	depends_on("py-setuptools", type=("build"))
	with default_args(type=("build", "run")):
		depends_on("py-pyyaml")
