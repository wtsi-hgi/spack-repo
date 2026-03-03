# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantcurves(RPackage):
	"""Estimate Quantiles Curves

	Non-parametric methods as local normal regression, polynomial local regression and penalized cubic B-splines regression are used to estimate quantiles curves. See Fan and Gijbels (1996) <doi:10.1201/9780203748725> and Perperoglou et al.(2019) <doi:10.1186/s12874-019-0666-3>.
	"""
	
	cran = "quantCurves" 

	version("1.0.0", md5="fdae3e9973f23cd01a07616087508bce")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-quantreggrowth", type=("build", "run"))
