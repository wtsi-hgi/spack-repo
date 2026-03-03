# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkendall(RPackage):
	"""Matrix Kendall's Tau and Matrix Elliptical Factor Model

	Large-scale matrix-variate data have been widely observed nowadays in various research areas such as finance, signal processing and medical imaging. Modelling matrix-valued data by matrix-elliptical family not only provides a flexible way to handle heavy-tail property and tail dependencies, but also maintains the intrinsic row and column structure of random matrices. We proposed a new tool named matrix Kendall's tau which is efficient for analyzing random elliptical matrices. By applying this new type of Kendell’s tau to the matrix elliptical factor model, we propose a Matrix-type Robust Two-Step (MRTS) method to estimate the loading and factor spaces. See the details in He at al. (2022) <arXiv:2207.09633>. In this package, we provide the algorithms for calculating sample matrix Kendall's tau, the MRTS method and the Matrix Kendall's tau Eigenvalue-Ratio (MKER) method which is used for determining the number of factors.
	"""
	
	cran = "MKendall" 

	version("1.5-4", md5="92a0438fc7081bf977b904c08f0ca952")

