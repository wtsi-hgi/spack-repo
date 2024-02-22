# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpls(RPackage):
	"""Robust Partial Least Squares

	A robust Partial Least-Squares (PLS) method is implemented that is robust to outliers in the residuals as well as to leverage points. A specific weighting scheme is applied which avoids iterations, and leads to a highly efficient robust PLS estimator.
	"""
	
	cran = "rpls" 

	version("0.6.0", md5="6546871d3826d41ba3e172179625d4d5")

	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
