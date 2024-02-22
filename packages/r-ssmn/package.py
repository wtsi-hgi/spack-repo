# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsmn(RPackage):
	"""Skew Scale Mixtures of Normal Distributions

	Performs the EM algorithm for regression models using Skew Scale Mixtures of Normal Distributions.
	"""
	
	cran = "ssmn" 

	version("1.1", md5="b1780cf0b06db2bb2a03e5dde67b4d1f")

	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
