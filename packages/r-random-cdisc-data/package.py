# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomCdiscData(RPackage):
	"""Create Random ADaM Datasets

	A set of functions to create random Analysis Data Model (ADaM) datasets and cached dataset.
    ADaM dataset specifications are described by the Clinical Data Interchange Standards Consortium (CDISC) 
    Analysis Data Model Team.
	"""
	
	cran = "random.cdisc.data" 

	version("0.3.15", md5="e872aa3cb7a245953f2b45d39b590386")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-yaml@2.1.19:", type=("build", "run"))
