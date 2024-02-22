# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZvcv(RPackage):
	"""Zero-Variance Control Variates

	Stein control variates can be used to improve Monte Carlo estimates of expectations when the derivatives of the log target are available. This package implements a variety of such methods, including zero-variance control variates (ZV-CV, Mira et al. (2013) <doi:10.1007/s11222-012-9344-6>), regularised ZV-CV (South et al., 2018 <arXiv:1811.05073>), control functionals (CF, Oates et al. (2017) <doi:10.1111/rssb.12185>) and semi-exact control functionals (SECF, South et al., 2020 <arXiv:2002.00033>). ZV-CV is a parametric approach that is exact for (low order) polynomial integrands with Gaussian targets. CF is a non-parametric alternative that offers better than the standard Monte Carlo convergence rates. SECF has both a parametric and a non-parametric component and it offers the advantages of both for an additional computational cost. Functions for applying ZV-CV and CF to two estimators for the normalising constant of the posterior distribution in Bayesian statistics are also supplied in this package. The basic requirements for using the package are a set of samples, derivatives and function evaluations. 
	"""
	
	cran = "ZVCV" 

	version("2.1.2", md5="f2dbdcc1c6510ae621deb2f6cec290c0")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rlinsolve", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
