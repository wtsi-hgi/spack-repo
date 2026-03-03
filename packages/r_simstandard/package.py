# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimstandard(RPackage):
	"""Generate Standardized Data

	Creates simulated data from structural equation models with standardized loading. Data generation methods are described in Schneider (2013) <doi:10.1177/0734282913478046>.
	"""
	
	homepage = "https://github.com/wjschne/simstandard"
	cran = "simstandard" 

	version("0.6.3", md5="2cb3001262c61332259a2d910861ae05")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
