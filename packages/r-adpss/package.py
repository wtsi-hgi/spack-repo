# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdpss(RPackage):
	"""Design and Analysis of Locally or Globally Efficient Adaptive
Designs

	Provides the functions for planning and conducting a
  clinical trial with adaptive sample size determination. Maximal statistical
  efficiency will be exploited even when dramatic or multiple adaptations
  are made. Such a trial consists of adaptive determination of sample size
  at an interim analysis and implementation of frequentist statistical test at the
  interim and final analysis with a prefixed significance level. The required
  assumptions for the stage-wise test statistics are independent and stationary
  increments and normality. Predetermination of adaptation rule is not required.
	"""
	
	homepage = "https://github.com/ca4wa/R-adpss"
	cran = "adpss" 

	version("0.1.2", md5="cfecc0b0ce0d1e3eacf5b93491f14975")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.17:", type=("build", "run"))
