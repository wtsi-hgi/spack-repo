# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLordif(RPackage):
	"""Logistic Ordinal Regression Differential Item Functioning using
IRT

	Analysis of Differential Item Functioning (DIF) for
        dichotomous and polytomous items using an iterative hybrid of
        ordinal logistic regression and item response theory (IRT).
	"""
	
	cran = "lordif" 

	version("0.3-3", md5="a4b6777b04e5267c031680a7b2134bfb")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
