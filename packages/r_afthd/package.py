# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfthd(RPackage):
	"""Accelerated Failure Time for High Dimensional Data with MCMC

	Functions for Posterior estimates of Accelerated Failure Time(AFT) model with MCMC and Maximum likelihood estimates of AFT model without MCMC for univariate and multivariate analysis in high dimensional gene expression data are available in this 'afthd' package.
            AFT model with Bayesian framework for multivariate in high dimensional data has been proposed by Prabhash et al.(2016)
             <doi:10.21307/stattrans-2016-046>.
	"""
	
	cran = "afthd" 

	version("1.1.0", md5="29833cd7761403994fdc101296572f97")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-photobiology", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-rstpm2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
