# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapbayr(RPackage):
	"""MAP-Bayesian Estimation of PK Parameters

	Performs maximum a posteriori Bayesian estimation of individual pharmacokinetic parameters from a model defined in 'mrgsolve', typically for model-based therapeutic drug monitoring. Internally computes an objective function value from model and data, performs optimization and returns predictions in a convenient format. The performance of the package was described by Le Louedec et al (2021) <doi:10.1002/psp4.12689>.
	"""
	
	homepage = "https://github.com/FelicienLL/mapbayr"
	cran = "mapbayr" 

	version("0.10.0", md5="920133288e565c0460a5761c02fbe3ea")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mrgsolve@1.0.8:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
