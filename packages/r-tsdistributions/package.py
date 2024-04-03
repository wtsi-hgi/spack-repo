# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdistributions(RPackage):
	"""Location Scale Standardized Distributions

	Location-Scale based distributions parameterized in terms of mean, standard deviation, skew and shape parameters and estimation using automatic differentiation. Distributions include the Normal, Student and GED as well as their skewed variants ('Fernandez and Steel'), the 'Johnson SU', and the Generalized Hyperbolic.
	"""
	
	homepage = "https://www.nopredict.com/packages/tsdistributions"
	cran = "tsdistributions" 

	version("1.0.0", md5="62d0384cac1e231451add80441e8c002")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tsmethods", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-generalizedhyperbolic", type=("build", "run"))
	depends_on("r-skewhyperbolic", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
