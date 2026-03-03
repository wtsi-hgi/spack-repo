# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsem(RPackage):
	"""Fit Dynamic Structural Equation Models

	Applies dynamic structural equation models to time-series data
	with generic and simplified specification for simultaneous and lagged
	effects. Methods are described in Thorson et al. (2024)
	"Dynamic structural equation models synthesize ecosystem dynamics 
	constrained by ecological mechanisms."  
	"""
	
	homepage = "https://james-thorson-noaa.github.io/dsem/"
	cran = "dsem" 

	version("1.2.1", md5="4d88bcb5e8b509eda21864e3dfde6975")
	version("1.1.0", md5="2e8c94f6c86afcafd730aaf9917475c8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
