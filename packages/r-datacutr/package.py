# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatacutr(RPackage):
	"""SDTM Datacut

	Supports the process of applying a cut to Standard Data Tabulation Model (SDTM),
    as part of the analysis of specific points in time of the data, normally as part of 
    investigation into clinical trials. The functions support different approaches of
    cutting to the different domains of SDTM normally observed.
	"""
	
	cran = "datacutr" 

	version("0.1.0", md5="bc60c502a5d075683468dd721f3e1808")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-admiraldev", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
