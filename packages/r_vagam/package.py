# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVagam(RPackage):
	"""Variational Approximations for Generalized Additive Models

	Fits generalized additive models (GAMs) using a variational approximations (VA) framework. In brief, the VA framework provides a fully or at least closed to fully tractable lower bound approximation to the marginal likelihood of a GAM when it is parameterized as a mixed model (using penalized splines, say). In doing so, the VA framework aims offers both the stability and natural inference tools available in the mixed model approach to GAMs, while achieving computation times comparable to that of using the penalized likelihood approach to GAMs. See Hui et al. (2018) <doi:10.1080/01621459.2018.1518235>.
	"""
	
	cran = "vagam" 

	version("1.1", md5="d55ce7618e889ad896cedc82b0530e9a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
