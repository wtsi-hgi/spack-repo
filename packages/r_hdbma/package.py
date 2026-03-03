# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdbma(RPackage):
	"""Bayesian Mediation Analysis with High-Dimensional Data

	Mediation analysis is used to identify and quantify intermediate effects from factors that intervene the observed relationship between an exposure/predicting variable and an outcome. We use a Bayesian adaptive lasso method to take care of the hierarchical structures and high dimensional exposures or mediators.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "hdbma" 

	version("1.0", md5="5e21aab386c23fa69639aef226e5c59a")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
