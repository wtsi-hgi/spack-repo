# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwang(RPackage):
	"""Toolkit for Weighting and Analysis of Nonequivalent Groups

	Provides functions for propensity score
        estimating and weighting, nonresponse weighting, and diagnosis
        of the weights.
	"""
	
	cran = "twang" 

	version("2.6", md5="715b352d926e61d7c3757a952c3980e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gbm@1.5.3:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
