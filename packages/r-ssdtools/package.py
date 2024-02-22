# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsdtools(RPackage):
	"""Species Sensitivity Distributions

	Species sensitivity distributions are cumulative probability
    distributions which are fitted to toxicity concentrations for
    different species as described by Posthuma et al.(2001)
    <isbn:9781566705783>.  The ssdtools package uses Maximum Likelihood to
    fit distributions such as the gamma, log-logistic, log-normal and
    Weibull to censored and/or weighted data.  Multiple distributions can
    be averaged using Akaike Information Criteria.  Confidence intervals
    on hazard concentrations and proportions are produced by parametric
    bootstrapping.
	"""
	
	homepage = "https://github.com/bcgov/ssdtools"
	cran = "ssdtools" 

	version("1.0.6", md5="4fe9cc1cf1afc46135f7991f07836100")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ssddata", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-universals", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
