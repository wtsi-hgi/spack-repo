# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnireg(RPackage):
	"""Unimodal Penalized Spline Regression using B-Splines

	Univariate spline regression. It is possible to add the shape constraint of unimodality and predefined or
	self-defined penalties on the B-spline coefficients.
	"""
	
	cran = "uniReg" 

	version("1.1", md5="b8b9f476aceac7c2e80e65a501e4a0c5")

	depends_on("r-dosefinding", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-sel", type=("build", "run"))
