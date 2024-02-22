# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvtools(RPackage):
	"""Instrumental Variables

	Contains tools for instrumental variables estimation. Currently, non-parametric bounds, two-stage estimation and G-estimation are implemented. Balke, A. and Pearl, J. (1997) <doi:10.2307/2965583>, Vansteelandt S., Bowden J., Babanezhad M., Goetghebeur E. (2011) <doi:10.1214/11-STS360>. 
	"""
	
	cran = "ivtools" 

	version("2.3.0", md5="193f45531fd807b35bf2c0d19d47025a")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ahaz", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
