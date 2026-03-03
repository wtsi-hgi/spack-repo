# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedpoisson(RPackage):
	"""Mixed Poisson Models

	The estimation of the parameters in mixed Poisson models. 
	"""
	
	cran = "MixedPoisson" 

	version("2.0", md5="203723f6b21eaea18e375362042112d4")

	depends_on("r-gaussquad", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
