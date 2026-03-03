# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSizemat(RPackage):
	"""Estimate Size at Sexual Maturity

	Estimate morphometric and gonadal size at sexual maturity for organisms, usually fish and invertebrates. It includes methods for classification based on relative growth (using principal components analysis, hierarchical clustering, discriminant analysis), logistic regression (Frequentist or Bayes), parameters estimation and some basic plots.
	"""
	
	cran = "sizeMat" 

	version("1.1.2", md5="592e9d0c26d787c38625ce5a73e54b13")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
