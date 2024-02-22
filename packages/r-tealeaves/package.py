# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealeaves(RPackage):
	"""Solve for Leaf Temperature Using Energy Balance

	Implements models of leaf temperature using energy balance. It uses units to ensure that parameters are properly specified and transformed before calculations. It allows separate lower and upper surface conductances to heat and water vapour, so sensible and latent heat loss are calculated for each surface separately  as in Foster and Smith (1986) <doi:10.1111/j.1365-3040.1986.tb02108.x>. It's straightforward to model leaf temperature over environmental gradients such as light, air temperature, humidity, and wind. It can also model leaf temperature over trait gradients such as leaf size or stomatal conductance. Other references are Monteith and Unsworth (2013, ISBN:9780123869104), Nobel (2009, ISBN:9780123741431), and Okajima et al. (2012) <doi:10.1007/s11284-011-0905-5>.
	"""
	
	cran = "tealeaves" 

	version("1.0.6", md5="b30632b1d62a1af5357cdbef7073bfe5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-units@0.6:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-crayon@1.3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-furrr@0.1:", type=("build", "run"))
	depends_on("r-future@1.10:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
