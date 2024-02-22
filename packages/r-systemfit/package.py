# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSystemfit(RPackage):
	"""Estimating Systems of Simultaneous Equations

	Econometric estimation of simultaneous
 systems of linear and nonlinear equations using Ordinary Least
 Squares (OLS), Weighted Least Squares (WLS), Seemingly Unrelated
 Regressions (SUR), Two-Stage Least Squares (2SLS), Weighted
 Two-Stage Least Squares (W2SLS), and Three-Stage Least Squares (3SLS)
 as suggested, e.g., by Zellner (1962) <doi:10.2307/2281644>,
 Zellner and Theil (1962) <doi:10.2307/1911287>, and
 Schmidt (1990) <doi:10.1016/0304-4076(90)90127-F>.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/systemfit/"
	cran = "systemfit" 

	version("1.1-30", md5="ce0cf8a69c9c3c0f916c2d32770803c1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-car@2.0.0:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-sandwich@2.2.9:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
