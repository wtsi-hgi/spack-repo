# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrototest(RPackage):
	"""Inference on Prototypes from Clusters of Features

	Procedures for testing for group-wide signal in clusters of variables. Tests can be performed for single groups in isolation (univariate) or multiple groups together (multivariate). Specific tests include the exact and approximate (un)selective likelihood ratio tests described in Reid et al (2015), the selective F test and marginal screening prototype test of Reid and Tibshirani (2015). User may pre-specify columns to be included in prototype formation, or allow the function to select them itself. A mixture of these two is also possible. Any variable selection is accounted for using the selective inference framework. Options for non-sampling and hit-and-run null reference distributions.
	"""
	
	homepage = "http://arxiv.org/abs/1511.07839"
	cran = "prototest" 

	version("1.2", md5="a7f9bd1865b4f67838af0a3976074de6")

	depends_on("r-intervals", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
