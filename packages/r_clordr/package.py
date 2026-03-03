# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClordr(RPackage):
	"""Composite Likelihood Inference and Diagnostics for Replicated
Spatial Ordinal Data

	Composite likelihood parameter estimate and asymptotic covariance matrix are calculated for the spatial ordinal data with replications, where spatial ordinal response with covariate and both spatial exponential covariance within subject and independent and identically distributed measurement error.  Parameter estimation can be performed by either solving the gradient function or maximizing composite log-likelihood. Parametric bootstrapping is used to estimate the Godambe information matrix and hence the asymptotic standard error and covariance matrix with parallel processing option. Moreover, the proposed surrogate residual, which extends the results of Liu and Zhang (2017) <doi: 10.1080/01621459.2017.1292915>, can act as a useful tool for model diagnostics.
	"""
	
	cran = "clordr" 

	version("1.7.0", md5="12bb9300a3540d33a2af006748a3594f")

	depends_on("r-pbivnorm@0.6:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-rootsolve@1.7:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-foreach@1.2:", type=("build", "run"))
	depends_on("r-tmvmixnorm@1.0.2:", type=("build", "run"))
