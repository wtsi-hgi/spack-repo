# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdehabitathr(RPackage):
	"""Home Range Estimation

	A collection of tools for the estimation of animals home range.
	"""
	
	cran = "adehabitatHR" 

	version("0.4.21", md5="65e0cd82d437ba6b0dc01cba846b65f5")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-adehabitatma", type=("build", "run"))
	depends_on("r-adehabitatlt", type=("build", "run"))
