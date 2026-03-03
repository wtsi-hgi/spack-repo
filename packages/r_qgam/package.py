# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgam(RPackage):
	"""Smooth Additive Quantile Regression Models

	Smooth additive quantile regression models, fitted using
    the methods of Fasiolo et al. (2020) <doi:10.1080/01621459.2020.1725521>.
    See Fasiolo at al. (2021) <doi:10.18637/jss.v100.i09> for an introduction to the package. Differently from
    'quantreg', the smoothing parameters are estimated automatically by marginal
    loss minimization, while the regression coefficients are estimated using either
    PIRLS or Newton algorithm. The learning rate is determined so that the Bayesian
    credible intervals of the estimated effects have approximately the correct
    coverage. The main function is qgam() which is similar to gam() in 'mgcv', but
    fits non-parametric quantile regression models.
	"""
	
	cran = "qgam" 

	version("1.3.4", md5="c0dd6c556238941287a9417598878b68")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv@1.8.28:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
