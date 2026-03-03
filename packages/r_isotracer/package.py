# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsotracer(RPackage):
	"""Isotopic Tracer Analysis Using MCMC

	Implements Bayesian models to analyze data from tracer addition
    experiments. The implemented method was originally described in the article
    "A New Method to Reconstruct Quantitative Food Webs and Nutrient Flows from
    Isotope Tracer Addition Experiments" by López-Sepulcre et al. (2020)
    <doi:10.1086/708546>.
	"""
	
	homepage = "https://gitlab.com/matthieu-bruneaux/isotracer"
	cran = "isotracer" 

	version("1.1.5", md5="763a1c50e46eaab12a14ee413cd8c293")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-coda@0.19.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-latex2exp@0.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pillar@1.4.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-bh@1.72:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.7:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
