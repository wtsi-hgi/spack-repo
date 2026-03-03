# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMets(RPackage):
	"""Analysis of Multivariate Event Times

	Implementation of various statistical models for multivariate
    event history data <doi:10.1007/s10985-013-9244-x>. Including multivariate
    cumulative incidence models <doi:10.1002/sim.6016>, and  bivariate random
    effects probit models (Liability models) <doi:10.1016/j.csda.2015.01.014>.
    Modern methods for survival analysis, including regression modelling (Cox, Fine-Gray, 
    Ghosh-Lin, Binomial regression) with fast computation of influence functions. 
	"""
	
	homepage = "https://kkholst.github.io/mets/"
	cran = "mets" 

	version("1.3.4", md5="98f12a27601850db18260ea75893676a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-timereg@1.9.4:", type=("build", "run"))
	depends_on("r-lava@1.7.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival@2.43.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
