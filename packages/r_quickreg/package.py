# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickreg(RPackage):
	"""Build Regression Models Quickly and Display the Results Using
'ggplot2'

	A set of functions to extract results from regression models and
 plot the effect size using 'ggplot2' seamlessly. While 'broom' is useful to
 convert statistical analysis objects into tidy data frames, 'coefplot' is adept at showing
 multivariate regression results. With specific outcome, this package could build regression models
 automatically, extract results into a data frame and provide a quicker way to summarize
 models' statistical findings using 'ggplot2'.
	"""
	
	cran = "quickReg" 

	version("1.5.0", md5="6e4ca986a9f6f62614e55abb6a6967bb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
