# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputerobust(RPackage):
	"""Robust Multiple Imputation with Generalized Additive Models for
Location Scale and Shape

	Provides new imputation methods for the 'mice' package based on generalized additive models for location, scale, and shape (GAMLSS) as described in de Jong, van Buuren and Spiess <doi:10.1080/03610918.2014.911894>.
	"""
	
	cran = "ImputeRobust" 

	version("1.3-1", md5="2c418b8127cf225f18fa0af6fccc7a40")

	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-extremevalues", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
