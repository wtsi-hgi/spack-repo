# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsosvm(RPackage):
	"""Stream Suitable Online Support Vector Machines

	Soft-margin support vector machines (SVMs) are a common class of classification models. The training of SVMs usually requires that the data be available all at once in a single batch, however the Stochastic majorization-minimization (SMM) algorithm framework allows for the training of SVMs on streamed data instead Nguyen, Jones & McLachlan(2018)<doi:10.1007/s42081-018-0001-y>. This package utilizes the SMM framework to provide functions for training SVMs with hinge loss, squared-hinge loss, and logistic loss.
	"""
	
	cran = "SSOSVM" 

	version("0.2.1", md5="32b5b767ef1ce29cd5985e969bb0e743")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
