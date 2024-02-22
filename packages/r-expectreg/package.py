# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpectreg(RPackage):
	"""Expectile and Quantile Regression

	Expectile and quantile regression of models with nonlinear effects
  e.g. spatial, random, ridge using least asymmetric weighed squares / absolutes
  as well as boosting; also supplies expectiles for common distributions.
	"""
	
	cran = "expectreg" 

	version("0.53", md5="a71fa927b0c950514dbc19013adc0e8d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mboost@2.1:", type=("build", "run"))
	depends_on("r-bayesx@0.2.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-colorspace@0.97:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
