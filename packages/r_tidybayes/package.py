# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidybayes(RPackage):
	"""Tidy Data and 'Geoms' for Bayesian Models

	Compose data for and extract, manipulate, and visualize posterior draws from Bayesian models
    ('JAGS', 'Stan', 'rstanarm', 'brms', 'MCMCglmm', 'coda', ...) in a tidy data format. Functions are provided
    to help extract tidy data frames of draws from Bayesian models and that generate point
    summaries and intervals in a tidy format. In addition, 'ggplot2' 'geoms' and 'stats' are provided for
    common visualization primitives like points with multiple uncertainty intervals, eye plots (intervals plus
    densities), and fit curves with multiple, arbitrary uncertainty bands.
	"""
	
	homepage = "https://mjskay.github.io/tidybayes/"
	cran = "tidybayes" 

	version("3.0.6", md5="2110128f103827efaae10a24012fdd58")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggdist@3:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-arrayhelpers", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-posterior@1.0.1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
