# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFregression(RPackage):
	"""Rmetrics - Regression Based Decision and Prediction

	A collection of functions for linear and non-linear regression 
  modelling. It implements a wrapper for several regression models available 
  in the base and contributed packages of R. 
	"""
	
	homepage = "https://www.rmetrics.org"
	cran = "fRegression" 

	version("4021.83", md5="c42fe4638928d23f4c047211a7ab7b75")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-polspline", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
