# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaehbMe(RPackage):
	"""Small Area Estimation with Measurement Error using Hierarchical
Bayesian Method

	Implementation of small area estimation using Hierarchical Bayesian (HB) Method when auxiliary variable measured with error. The 'rjags' package is employed to obtain parameter estimates. For the references, see Rao and Molina (2015) <doi:10.1002/9781118735855>, Ybarra and Lohr (2008) <doi:10.1093/biomet/asn048>, and Ntzoufras (2009, ISBN-10: 1118210352).  
	"""
	
	cran = "saeHB.ME" 

	version("1.0.1", md5="ca5b7b2239e3abf93f8fae042a5e2fb5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
