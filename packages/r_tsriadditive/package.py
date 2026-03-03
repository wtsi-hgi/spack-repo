# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsriadditive(RPackage):
	"""Two Stage Residual Inclusion Additive Hazards Estimator

	Additive hazards models with two stage residual inclusion method are fitted under either survival data or competing risks data. The estimator incorporates an instrumental variable and therefore can recover causal estimand in the presence of unmeasured confounding under some assumptions. A.Ying, R. Xu and J. Murphy. (2019) <doi:10.1002/sim.8071>.
	"""
	
	homepage = "https://onlinelibrary.wiley.com/doi/abs/10.1002/sim.8071"
	cran = "tsriadditive" 

	version("1.0.0", md5="d9a431d740d75e63623560954da66be2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
