# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlasso(RPackage):
	"""Implementation of Adaptive or Non-Adaptive Differentiable Lasso
and SCAD Penalties in Linear Models

	An implementation of the differentiable lasso (dlasso) and SCAD (dSCAD) using iterative ridge algorithm. This package allows selecting the tuning parameter by AIC, BIC, GIC and GIC.
	"""
	
	homepage = "http://hamedhaseli.webs.com"
	cran = "DLASSO" 

	version("2.0.2", md5="e13b0ba4964e83d77e4c2a78e9f11aca")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
