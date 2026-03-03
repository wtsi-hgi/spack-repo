# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpsurvss(RPackage):
	"""Sample Size and Power Calculation for Common Non-Parametric
Tests in Survival Analysis

	A number of statistical tests have been proposed to compare two 
  survival curves, including the difference in (or ratio of) t-year 
  survival, difference in (or ratio of) p-th percentile survival, difference in
  (or ratio of) restricted mean survival time, and the weighted log-rank test. 
  Despite the multitude of options, the convention in survival studies is to assume
  proportional hazards and to use the unweighted log-rank test for design and 
  analysis. This package provides sample size and power 
  calculation for all of the above statistical tests with allowance for 
  flexible accrual, censoring, and survival (eg. Weibull, piecewise-exponential, 
  mixture cure). It is the companion R package to the paper by Yung and Liu (2019)
  <doi:10.1111/biom.13196>. Specific to the weighted log-rank test, users may 
  specify which approximations they wish to use to estimate the large-sample mean 
  and variance. The default option has been shown to provide substantial
  improvement over the conventional sample size and power equations based on Schoenfeld 
  (1981) <doi:10.1093/biomet/68.1.316>.
	"""
	
	homepage = "http://github.com/godwinyung/npsurvSS"
	cran = "npsurvSS" 

	version("1.0.1", md5="84f56ac18213622575aa5bd79755c1e9")

	depends_on("r@3.4:", type=("build", "run"))
