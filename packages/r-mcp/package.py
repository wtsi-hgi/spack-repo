# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcp(RPackage):
	"""Regression with Multiple Change Points

	Flexible and informed regression with Multiple Change Points. 'mcp' can infer change points in means, variances, autocorrelation structure, and any combination of these, as well as the parameters of the segments in between. All parameters are estimated with uncertainty and prediction intervals are supported - also near the change points. 'mcp' supports hypothesis testing via Savage-Dickey density ratio, posterior contrasts, and cross-validation. 'mcp' is described in Lindeløv (submitted) <doi:10.31219/osf.io/fzqxv> and generalizes the approach described in Carlin, Gelfand, & Smith (1992) <doi:10.2307/2347570> and Stephens (1994) <doi:10.2307/2986119>.
	"""
	
	homepage = "https://lindeloev.github.io/mcp/"
	cran = "mcp" 

	version("0.3.4", md5="4a5dbc703f403586ed6ce2bf75f1dad5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-future@1.16:", type=("build", "run"))
	depends_on("r-future-apply@1.4:", type=("build", "run"))
	depends_on("r-rjags@4.9:", type=("build", "run"))
	depends_on("r-coda@0.19.3:", type=("build", "run"))
	depends_on("r-loo@2.1:", type=("build", "run"))
	depends_on("r-bayesplot@1.7:", type=("build", "run"))
	depends_on("r-tidybayes@3:", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@0.2.5:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-patchwork@1:", type=("build", "run"))
	depends_on("r-rlang@0.4.1:", type=("build", "run"))
