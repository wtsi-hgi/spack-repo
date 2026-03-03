# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlfpca(RPackage):
	"""Sparse Logistic Functional Principal Component Analysis

	Implementation for sparse logistic functional principal component analysis (SLFPCA). SLFPCA is specifically developed for functional binary data, and the estimated eigenfunction can be strictly zero on some sub-intervals, which is helpful for interpretation. The crucial function of this package is SLFPCA().
	"""
	
	cran = "SLFPCA" 

	version("3.0", md5="6d511b7994af74f2c413b39863e68610")

	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
