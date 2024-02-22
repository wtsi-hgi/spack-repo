# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgglmm(RPackage):
	"""Estimate Quantitative Genetics Parameters from Generalised
Linear Mixed Models

	Compute various quantitative genetics parameters from a Generalised Linear Mixed Model (GLMM) estimates. Especially, it yields the observed phenotypic mean, phenotypic variance and additive genetic variance.
	"""
	
	cran = "QGglmm" 

	version("0.7.4", md5="83fdb590e9d13f552c5cdf37a27124a5")

	depends_on("r-cubature@1.4:", type=("build", "run"))
