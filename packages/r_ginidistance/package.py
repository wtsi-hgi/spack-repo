# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGinidistance(RPackage):
	"""A New Gini Correlation Between Quantitative and Qualitative
Variables

	An implementation of a new Gini covariance and correlation to measure dependence between a categorical and numerical variables. Dang, X., Nguyen, D., Chen, Y. and Zhang, J., (2018) <arXiv:1809.09793>. 
	"""
	
	cran = "GiniDistance" 

	version("0.1.1", md5="4d9ebbc05909f3495a9917631a12405a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
