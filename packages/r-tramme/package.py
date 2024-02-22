# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTramme(RPackage):
	"""Transformation Models with Mixed Effects

	Likelihood-based estimation of mixed-effects transformation models
    using the Template Model Builder ('TMB', Kristensen et al., 2016)
    <doi:10.18637/jss.v070.i05>. The technical details of transformation models
    are given in Hothorn et al. (2018) <doi:10.1111/sjos.12291>. Likelihood
    contributions of exact, randomly censored (left, right, interval) and
    truncated observations are supported. The random effects are assumed to be
    normally distributed on the scale of the transformation function, the
    marginal likelihood is evaluated using the Laplace approximation, and the
    gradients are calculated with automatic differentiation (Tamasi & Hothorn,
    2021) <doi:10.32614/RJ-2021-075>. Penalized smooth shift terms can be
    defined using 'mgcv'.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "tramME" 

	version("1.0.5", md5="f082f32681b3f799349253ff9bbcb46c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tram@0.3.2:", type=("build", "run"))
	depends_on("r-mlt@1.1:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-lme4@1.1.19:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv@1.8.34:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-variables@1.0.2:", type=("build", "run"))
	depends_on("r-basefun@1.0.6:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-coneproj", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
