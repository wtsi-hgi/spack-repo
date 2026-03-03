# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexsurv(RPackage):
	"""Flexible Parametric Survival and Multi-State Models

	Flexible parametric models for time-to-event data,
    including the Royston-Parmar spline model, generalized gamma and
    generalized F distributions.  Any user-defined parametric
    distribution can be fitted, given at least an R function defining
    the probability density or hazard. There are also tools for
    fitting and predicting from fully parametric multi-state models,
    based on either cause-specific hazards or mixture models.
	"""
	
	homepage = "https://github.com/chjackson/flexsurv-dev"
	cran = "flexsurv" 

	version("2.3.2", md5="b46668f4d46554e6dc90fd6a0bb54f7f")
	version("2.2.2", md5="a86c5647062c60b2bebb5ffb8165604f")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mstate@0.2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-muhaz", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstpm2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
