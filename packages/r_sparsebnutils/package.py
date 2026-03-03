# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsebnutils(RPackage):
	"""Utilities for Learning Sparse Bayesian Networks

	A set of tools for representing and estimating sparse Bayesian networks from continuous and discrete data, as described in Aragam, Gu, and Zhou (2017) <arXiv:1703.04025>.
	"""
	
	homepage = "https://github.com/itsrainingdata/sparsebnUtils"
	cran = "sparsebnUtils" 

	version("0.0.8", md5="1517d36ea36652702bd7b113b0b776b6")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
