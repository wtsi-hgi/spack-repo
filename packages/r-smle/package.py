# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmle(RPackage):
	"""Joint Feature Screening via Sparse MLE

	Feature screening is a powerful tool in processing ultrahigh dimensional data. It attempts to screen out most irrelevant features in preparation for a more elaborate analysis. Xu and Chen (2014)<doi:10.1080/01621459.2013.879531> proposed an effective screening method SMLE, which naturally incorporates the joint effects among features in the screening process. This package provides an efficient implementation of SMLE-screening for high-dimensional linear, logistic, and Poisson models. The package also provides a function for conducting accurate post-screening feature selection based on an iterative hard-thresholding procedure and a user-specified selection criterion.
	"""
	
	cran = "SMLE" 

	version("2.1-1", md5="d7100befd923705b429a2ce91bc20f4b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
