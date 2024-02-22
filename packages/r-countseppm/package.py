# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountseppm(RPackage):
	"""Mean and Variance Modeling of Count Data

	Modeling under- and over-dispersed count data using extended Poisson process models as in the article Faddy and Smith (2011) <doi:10.18637/jss.v069.i06> .
	"""
	
	cran = "CountsEPPM" 

	version("3.1", md5="9ec0f502798b7c72c159f916f86ace57")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
