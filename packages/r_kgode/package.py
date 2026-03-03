# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKgode(RPackage):
	"""Kernel Based Gradient Matching for Parameter Inference in
Ordinary Differential Equations

	The kernel ridge regression and the gradient matching algorithm proposed in Niu et al. (2016) <https://proceedings.mlr.press/v48/niu16.html> and the warping algorithm proposed in Niu et al. (2017) <DOI:10.1007/s00180-017-0753-z> are implemented for parameter inference in differential equations. Four schemes are provided for improving parameter estimation in odes by using the odes regularisation and warping.
	"""
	
	cran = "KGode" 

	version("1.0.4", md5="0923f5743adda46b92547dd1e24f1dea")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-pspline", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
