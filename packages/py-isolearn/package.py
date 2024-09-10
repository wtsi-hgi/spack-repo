# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIsolearn(PythonPackage):
	"""Keras Genomics Data Generators"""
	
	homepage = "https://github.com/johli/isolearn"
	pypi = "isolearn/isolearn-0.2.1.tar.gz" 

	version("0.2.1", sha256="d0feaa7de079e360e01e9ac65f8197325aeec2bd126c0d0725f13b8ea46187b6", url="https://files.pythonhosted.org/packages/f3/1b/02a1acbf51862117e64967c6946db95d536505bd0a2002509cd0f525c937/isolearn-0.2.1.tar.gz")

	depends_on("py-keras", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
