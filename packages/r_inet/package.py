# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInet(RPackage):
	"""Performing Inference on Networks with Regularization

	Performs inference with the lasso in Gaussian Graphical Models. The package consists of wrappers for functions from the 'hdi' package.
	"""
	
	cran = "inet" 

	version("0.1.0", md5="693984be65d6ca3e40b57a0b1ae8bb7b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hdi", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
