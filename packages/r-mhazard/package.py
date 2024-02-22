# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhazard(RPackage):
	"""Nonparametric and Semiparametric Methods for Multivariate
Failure Time Data

	Nonparametric survival function estimates and semiparametric
    regression for the multivariate failure time data with right-censoring.
    For nonparametric survival function estimates, the Volterra, Dabrowska,
    and Prentice-Cai estimates for bivariate failure time data may be
    computed as well as the Dabrowska estimate for the trivariate failure
    time data. Bivariate marginal hazard rate regression can be fitted for
    the bivariate failure time data. Functions are also provided to compute
    (bootstrap) confidence intervals and plot the estimates of the bivariate
    survival function. For details, see "The Statistical Analysis of
    Multivariate Failure Time Data: A Marginal Modeling Approach", Prentice,
    R., Zhao, S. (2019, ISBN: 978-1-4822-5657-4), CRC Press.
	"""
	
	cran = "mhazard" 

	version("0.2.3", md5="b1149e7db8907bf2076a0fd769069047")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
