# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCepumd(RPackage):
	"""Calculate Consumer Expenditure Survey (CE) Annual Estimates

	Provides functions and data files to help CE Public-Use
    Microdata (PUMD) users calculate annual estimated expenditure means,
    standard errors, and quantiles according to the methods used by the CE with
    PUMD. For more information on the CE please visit <https://www.bls.gov/cex>.
    For further reading on CE estimate calculations please see the CE
    Calculation section of the U.S. Bureau of Labor Statistics (BLS) Handbook of
    Methods at <https://www.bls.gov/opub/hom/cex/calculation.htm>. For
    further information about CE PUMD please visit
    <https://www.bls.gov/cex/pumd.htm>.
	"""
	
	homepage = "https://arcenis-r.github.io/cepumd/"
	cran = "cepumd" 

	version("2.1.0", md5="d825ae4bab44a9379a14597f66ee1547")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
