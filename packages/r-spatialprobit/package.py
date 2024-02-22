# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialprobit(RPackage):
	"""Spatial Probit Models

	A collection of methods for the Bayesian estimation of Spatial Probit, Spatial Ordered Probit and Spatial Tobit Models. Original implementations from the works of 'LeSage and Pace' (2009, ISBN: 1420064258) were ported and adjusted for R, as described in 'Wilhelm and de Matos' (2013) <doi:10.32614/RJ-2013-013>.  
	"""
	
	homepage = "https://www.r-project.org"
	cran = "spatialprobit" 

	version("1.0.4", md5="d2ed05511b2951c27d40643a888f9f01")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spdep@1.1.1:", type=("build", "run"))
	depends_on("r-spatialreg@1.1.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
