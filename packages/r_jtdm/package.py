# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJtdm(RPackage):
	"""Joint Modelling of Functional Traits

	Fitting and analyzing a Joint Trait Distribution Model. The Joint Trait Distribution Model is implemented in the Bayesian framework using conjugate priors and posteriors, thus guaranteeing fast inference. In particular the package computes joint probabilities and multivariate confidence intervals, and enables the investigation of how they depend on the environment through partial response curves. The method implemented by the package is described in Poggiato et al. (2023) <doi:10.1111/geb.13706>.
	"""
	
	homepage = "https://github.com/giopogg/jtdm"
	cran = "jtdm" 

	version("0.1-2", md5="01708dcf8d76a76482bb97e0cb4257f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-mniw", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
