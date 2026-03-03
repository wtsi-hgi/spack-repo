# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwangcontinuous(RPackage):
	"""Toolkit for Weighting and Analysis of Nonequivalent Groups -
Continuous Exposures

	Provides functions for propensity score
        estimation and weighting for continuous exposures as described in Zhu, Y., 
        Coffman, D. L., & Ghosh, D. (2015). A boosting algorithm for
        estimating generalized propensity scores with continuous treatments.
        Journal of Causal Inference, 3(1), 25-40. <doi:10.1515/jci-2014-0022>.
	"""
	
	cran = "twangContinuous" 

	version("1.0.0", md5="7c46689a235651ecee1057bd73e37201")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.19:", type=("build", "run"))
	depends_on("r-lattice@0.20.35:", type=("build", "run"))
	depends_on("r-gbm@2.1.3:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
