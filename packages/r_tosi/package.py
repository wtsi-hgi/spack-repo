# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTosi(RPackage):
	"""Two-Directional Simultaneous Inference for High-Dimensional
Models

	A general framework of two directional simultaneous inference
    is provided for high-dimensional as well as the fixed dimensional models with manifest
    variable or latent variable structure, such as high-dimensional mean models, high-
    dimensional sparse regression models, and high-dimensional latent factors models.
    It is making the simultaneous inference on a set of parameters from two directions,
    one is testing whether the estimated zero parameters indeed are zero and the other is
    testing whether there exists zero in the parameter set of non-zero. More details can be 
    referred to Wei Liu, et al. (2022) <doi:10.48550/arXiv.2012.11100>.
	"""
	
	homepage = "https://github.com/feiyoung/TOSI"
	cran = "TOSI" 

	version("0.3.0", md5="17c336d6a96e10558ff10b606ab9b049")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hdi", type=("build", "run"))
	depends_on("r-scalreg", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
