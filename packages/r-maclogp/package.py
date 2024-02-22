# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaclogp(RPackage):
	"""Measures of Uncertainty for Model Selection

	Following the common types of measures of uncertainty for parameter estimation, two measures of uncertainty were proposed for model selection, see Liu, Li and Jiang (2020) <doi:10.1007/s11749-020-00737-9>. The first measure is a kind of model confidence set that relates to the variation of model selection, called Mac. The second measure focuses on error of model selection, called LogP. They are all computed via bootstrapping. This package provides functions to compute these two measures. Furthermore, a similar model confidence set adapted from Bayesian Model Averaging can also be computed using this package. 
	"""
	
	homepage = "https://github.com/YuanyuanLi96/maclogp"
	cran = "maclogp" 

	version("0.1.1", md5="c2a310dafed078c216455fafb4511f7c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bma", type=("build", "run"))
	depends_on("r-plot-matrix", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
