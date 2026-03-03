# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSilm(RPackage):
	"""Simultaneous Inference for Linear Models

	Simultaneous inference procedures for high-dimensional linear models as described by Zhang, X., and Cheng, G. (2017) <doi:10.1080/01621459.2016.1166114>.
	"""
	
	cran = "SILM" 

	version("1.0.0", md5="ce143a10e0bf5a6a0edbbdc29d4be6a6")

	depends_on("r-scalreg", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-hdi", type=("build", "run"))
	depends_on("r-sis", type=("build", "run"))
