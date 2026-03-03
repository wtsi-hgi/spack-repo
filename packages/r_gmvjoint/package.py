# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmvjoint(RPackage):
	"""Joint Models of Survival and Multivariate Longitudinal Data

	Fit joint models of survival and multivariate longitudinal data. The longitudinal
    data is specified by generalised linear mixed models. The joint models are fit via maximum
    likelihood using an approximate expectation maximisation algorithm. 
    Bernhardt (2015) <doi:10.1016/j.csda.2014.11.011>.
	"""
	
	homepage = "https://github.com/jamesmurray7/gmvjoint"
	cran = "gmvjoint" 

	version("0.4.0", md5="868d19f15bb693cfc08ce3b14d4085c5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
