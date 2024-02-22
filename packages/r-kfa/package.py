# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKfa(RPackage):
	"""K-Fold Cross Validation for Factor Analysis

	Provides functions to identify plausible and replicable factor
  structures for a set of variables via k-fold cross validation. The process
  combines the exploratory and confirmatory factor analytic approach to scale
  development (Flora & Flake, 2017) <doi:10.1037/cbs0000069> with a cross validation
  technique that maximizes the available data (Hastie, Tibshirani, & Friedman, 2009)
  <isbn:978-0-387-21606-5>. Also available are functions to determine k by drawing 
  on power analytic techniques for covariance structures (MacCallum, Browne, &
  Sugawara, 1996) <doi:10.1037/1082-989X.1.2.130>, generate model syntax, and
  summarize results in a report.
	"""
	
	homepage = "https://github.com/knickodem/kfa"
	cran = "kfa" 

	version("0.2.2", md5="97b2db58de8a410924365931c68f6e7d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-flextable@0.6.3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lavaan@0.6.9:", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-semtools@0.5.5:", type=("build", "run"))
	depends_on("r-simstandard", type=("build", "run"))
