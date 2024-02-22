# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHrqglas(RPackage):
	"""Group Variable Selection for Quantile and Robust Mean Regression

	A program that conducts group variable selection for quantile and robust mean 
              regression (Sherwood and Li, 2022). The group lasso penalty (Yuan and Lin, 2006) is used for
              group-wise variable selection. Both of the quantile and mean regression models are based on the Huber loss.
              Specifically, with the tuning parameter in the Huber loss approaching to 0, the quantile check 
              function can be approximated by the Huber loss for the median and the tilted version of 
              Huber loss at other quantiles. Such approximation provides computational efficiency and stability, and
              has also been shown to be statistical consistent.
	"""
	
	homepage = "GitHub:"
	cran = "hrqglas" 

	version("1.1.0", md5="1421def4b0edcdaf3f6e9ded987e168b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
