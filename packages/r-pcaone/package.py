# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcaone(RPackage):
	"""Randomized Singular Value Decomposition Algorithms with
'RcppEigen'

	Randomized Singular Value Decomposition (RSVD) methods proposed in the 'PCAone' paper by Li (2022) <doi:10.1101/2022.05.25.493261>, where we implement and propose two RSVD methods. One is based on Yu (2017) <arXiv:1704.07669> single pass RSVD but with power iteration scheme. The other is our new window based RSVD.
	"""
	
	homepage = "https://github.com/Zilong-Li/PCAoneR"
	cran = "pcaone" 

	version("1.0.0", md5="9429b3a74d5cfcd7c2a1aaf80045aebc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
