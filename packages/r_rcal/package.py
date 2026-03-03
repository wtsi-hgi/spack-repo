# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcal(RPackage):
	"""Regularized Calibrated Estimation

	Regularized calibrated estimation for causal inference and missing-data problems with high-dimensional data, based on Tan (2020a) <doi:10.1093/biomet/asz059>, Tan (2020b) <doi:10.1214/19-AOS1824> and Sun and Tan (2020) <arXiv:2009.09286>.
	"""
	
	homepage = "http://www.stat.rutgers.edu/~ztan"
	cran = "RCAL" 

	version("2.0", md5="443d29e53ec10abbcd628a00c4b548a9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
