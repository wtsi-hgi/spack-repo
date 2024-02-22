# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfrr(RPackage):
	"""Dichotomized Functional Response Regression

	Implementing Function-on-Scalar Regression model in which the response function is dichotomized and observed sparsely. This package provides smooth estimations of functional regression coefficients and principal components for the dichotomized functional response regression (dfrr) model.
	"""
	
	homepage = "https://github.com/asgari-fatemeh/dfrr"
	cran = "dfrr" 

	version("0.1.5", md5="920551a00ea909f9ba055ffa4b167790")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tmvtnorm@1.4.10:", type=("build", "run"))
	depends_on("r-fda@5.1.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
