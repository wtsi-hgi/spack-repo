# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsmediation(RPackage):
	"""Mediation Analysis Using Joint Significance

	A set of helper functions to conduct joint-significance tests
    for mediation analysis, as recommended by Yzerbyt, Muller, Batailler,
    & Judd. (2018) <doi:10.1037/pspa0000132>.
	"""
	
	homepage = "https://jsmediation.cedricbatailler.me/"
	cran = "JSmediation" 

	version("0.2.2", md5="cb9f6bc91d8e6545d6765303657b9d8e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.4.9:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
