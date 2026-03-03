# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDll(RPackage):
	"""Decorrelated Local Linear Estimator

	Implementation of the Decorrelated Local Linear estimator proposed 
    in <arxiv:1907.12732>. It constructs the confidence interval for the derivative 
    of the function of interest under the high-dimensional sparse additive model.
	"""
	
	homepage = "https://github.com/zijguo/HighDim-Additive-Inference"
	cran = "DLL" 

	version("1.0.0", md5="c1ca00935848170afa047d236705d69e")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-sam", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
