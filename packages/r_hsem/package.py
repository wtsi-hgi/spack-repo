# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsem(RPackage):
	"""Hierarchical Structural Equation Model

	We present this package for fitting structural equation models using the hierarchical likelihood method. This package allows extended structural equation model, including dynamic structural equation model. We illustrate the use of our packages with well-known data sets. Therefore, this package are able to handle two serious problems inadmissible solution and factor indeterminacy <doi:10.3390/sym13040657>.
	"""
	
	cran = "hsem" 

	version("1.0", md5="7ed3de923041bb9055c7c77c7a385adb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
