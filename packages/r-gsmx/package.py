# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsmx(RPackage):
	"""Multivariate Genomic Selection

	Estimating trait heritability and handling overfitting. This package includes a collection of functions for (1) estimating genetic variance-covariances and calculate trait heritability; and (2) handling overfitting by calculating the variance components and the heritability through cross validation.
	"""
	
	cran = "GSMX" 

	version("1.3", md5="219e1a66223fe3fb778aa53bbbecbcf1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
