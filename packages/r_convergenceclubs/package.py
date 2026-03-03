# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvergenceclubs(RPackage):
	"""Finding Convergence Clubs

	Functions for clustering regions that form convergence clubs, according to the definition of Phillips and Sul (2009) <doi:10.1002/jae.1080>. A package description is available in Sichera and Pizzuto (2019).
	"""
	
	homepage = "https://CRAN.R-project.org/package=ConvergenceClubs"
	cran = "ConvergenceClubs" 

	version("2.2.5", md5="6ee1abe3faebabcafccff2d614327ffb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lmtest@0.9.35:", type=("build", "run"))
	depends_on("r-sandwich@2.3.4:", type=("build", "run"))
