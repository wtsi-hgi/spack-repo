# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAftgee(RPackage):
	"""Accelerated Failure Time Model with Generalized Estimating
Equations

	A collection of methods for both the rank-based estimates and least-square estimates to the Accelerated Failure Time (AFT) model. For rank-based estimation, it provides approaches that include the computationally efficient Gehan's weight and the general's weight such as the logrank weight. Details of the rank-based estimation can be found in Chiou et al. (2014) <doi:10.1007/s11222-013-9388-2> and Chiou et al. (2015) <doi:10.1002/sim.6415>. For the least-square estimation, the estimating equation is solved with generalized estimating equations (GEE). Moreover, in multivariate cases, the dependence working correlation structure can be specified in GEE's setting. Details on the least-squares estimation can be found in Chiou et al. (2014) <doi:10.1007/s10985-014-9292-x>.
	"""
	
	homepage = "https://github.com/stc04003/aftgee"
	cran = "aftgee" 

	version("1.2.0", md5="bf74d951d5c4424f294ab0add2504936")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
