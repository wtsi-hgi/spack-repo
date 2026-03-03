# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmm(RPackage):
	"""Revenue Management Modeling

	The RMM  fits Revenue Management Models using the RDE(Robust Demand Estimation) method introduced in the paper by <doi:10.2139/ssrn.3598259>, one of the customer choice-based Revenue Management Model. Furthermore, it is possible to select a multinomial model as well as a conditional logit model as a model of RDE.
	"""
	
	cran = "RMM" 

	version("0.1.0", md5="7bbbb249963bf730cad7a7efc420c493")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
