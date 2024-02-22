# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensortest2d(RPackage):
	"""Fitting Second-Order Tensor Data

	An implementation of fitting generalized linear models on
    second-order tensor type data. The functions within this package mainly focus on
    parameter estimation, including parameter coefficients and standard deviation.
	"""
	
	homepage = "https://github.com/yuting1214/TensorTest2D"
	cran = "TensorTest2D" 

	version("1.1.1", md5="2d7823444d8521a5c3a480f7bba46927")

	depends_on("r@3.5:", type=("build", "run"))
