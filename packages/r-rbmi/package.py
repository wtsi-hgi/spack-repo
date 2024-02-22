# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbmi(RPackage):
	"""Reference Based Multiple Imputation

	Implements standard and reference based multiple imputation methods for continuous
    longitudinal endpoints (Gower-Page et al. (2022) <doi:10.21105/joss.04251>). In particular,
    this package supports deterministic conditional mean imputation and jackknifing as described
    in Wolbers et al.  (2022) <doi:10.1002/pst.2234>, Bayesian multiple imputation as described
    in Carpenter et al. (2013) <doi:10.1080/10543406.2013.834911>, and bootstrapped maximum
    likelihood imputation as described in von Hippel and Bartlett (2021) <doi: 10.1214/20-STS793>.
	"""
	
	homepage = "https://insightsengineering.github.io/rbmi/"
	cran = "rbmi" 

	version("1.2.6", md5="c853837af3193c4f9ded7731f184fb21")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mmrm", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
