# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBivgeom(RPackage):
	"""Roy's Bivariate Geometric Distribution

	Implements Roy's bivariate geometric model (Roy (1993) <doi:10.1006/jmva.1993.1065>): joint probability mass function, distribution function, survival function, random generation, parameter estimation, and more.
	"""
	
	cran = "bivgeom" 

	version("1.0", md5="ccdb86d1811d33815b0271e619a2255b")

	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
