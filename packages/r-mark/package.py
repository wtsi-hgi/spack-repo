# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMark(RPackage):
	"""Miscellaneous, Analytic R Kernels

	Miscellaneous functions and wrappers for development in other 
    packages created, maintained by Jordan Mark Barbone.
	"""
	
	homepage = "https://github.com/jmbarbone/mark"
	cran = "mark" 

	version("0.7.0", md5="0749dc0f3f473e20d33de171a6990ba8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fs@1.6.2:", type=("build", "run"))
	depends_on("r-fuj@0.1.4:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
