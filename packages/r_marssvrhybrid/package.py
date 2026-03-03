# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarssvrhybrid(RPackage):
	"""MARS SVR Hybrid

	Multivariate Adaptive Regression Spline (MARS) based Support Vector Regression (SVR) hybrid model is combined Machine learning hybrid approach which selects important variables using MARS and then fits SVR on the extracted important variables.
	"""
	
	cran = "MARSSVRhybrid" 

	version("0.1.0", md5="3c064749b78eef81768e626aa9d41f34")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
