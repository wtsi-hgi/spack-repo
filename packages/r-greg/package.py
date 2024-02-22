# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreg(RPackage):
	"""Regression Helper Functions

	Methods for manipulating regression models and for describing these in a style adapted for medical journals.
  Contains functions for generating an HTML table with crude and adjusted estimates, plotting hazard ratio, plotting model
  estimates and confidence intervals using forest plots, extending this to comparing multiple models in a single forest plots.
  In addition to the descriptive methods, there are functions for the robust covariance matrix provided by the 'sandwich'
  package, a function for adding non-linearities to a model, and a wrapper around the 'Epi' package's Lexis() functions for
  time-splitting a dataset when modeling non-proportional hazards in Cox regressions.
	"""
	
	homepage = "http://gforge.se"
	cran = "Greg" 

	version("2.0.2", md5="aaa180bab6ea2dc5e0943589f430c6fc")

	depends_on("r-gmisc@1.0.3:", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-epi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltable@2:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
