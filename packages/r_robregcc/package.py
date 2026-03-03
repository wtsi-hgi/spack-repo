# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobregcc(RPackage):
	"""Robust Regression with Compositional Covariates

	We implement the algorithm estimating the parameters of the robust regression model with compositional covariates. The model simultaneously treats outliers and provides reliable parameter  estimates. Publication reference: Mishra, A., Mueller, C.,(2019) <arXiv:1909.04990>.  
	"""
	
	homepage = "https://arxiv.org/abs/1909.04990"
	cran = "robregcc" 

	version("1.1", md5="d7e15d8fa83fb7e1157100ce44826f3e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
