# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLqmix(RPackage):
	"""Linear Quantile Mixture Models

	Estimate linear quantile mixtures based on Time-Constant (TC) and/or Time-Varying (TV), discrete, random coefficients.
	"""
	
	cran = "lqmix" 

	version("1.0", md5="0c64fcfc3cd9a180e0b943aaa8045b59")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
