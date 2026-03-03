# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynmix(RPackage):
	"""Estimation of Dynamic Finite Mixtures

	Allows to perform the dynamic mixture estimation with state-space components and normal regression components, and clustering with normal mixture. Quasi-Bayesian estimation, as well as, that based on the Kerridge inaccuracy approximation are implemented. Main references: Nagy and Suzdaleva (2013) <doi:10.1016/j.apm.2013.05.038>; Nagy et al. (2011) <doi:10.1002/acs.1239>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=dynmix"
	cran = "dynmix" 

	version("2.0", md5="3d08937b91dd1047b86a3bfca1cd5994")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
