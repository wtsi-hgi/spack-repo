# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsemse(RPackage):
	"""'Multiple Systems Estimation for Sparse Capture Data'

	Implements the routines and algorithms developed and analysed in "Multiple Systems Estimation for Sparse Capture Data: Inferential Challenges when there are Non-Overlapping Lists" Chan, L, Silverman, B. W., Vincent, K (2019) <arXiv:1902.05156>. This package explicitly handles situations where there are pairs of lists which have no observed individuals in common.  It deals correctly with parameters whose estimated values can be considered as being negative infinity.  It also addresses other possible issues of non-existence and non-identifiability of maximum likelihood estimates.
	"""
	
	homepage = "https://arxiv.org/abs/1902.05156"
	cran = "SparseMSE" 

	version("2.0.1", md5="8a6d8326087af8d6d192f0fae36bd150")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-rcapture", type=("build", "run"))
