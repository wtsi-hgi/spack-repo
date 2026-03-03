# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratamatch(RPackage):
	"""Stratification and Matching for Large Observational Data Sets

	A pilot matching design to automatically 
    stratify and match large datasets.  The manual_stratify() function allows
    users to manually stratify a dataset based on categorical variables of 
    interest, while the auto_stratify() function does automatically by
    allocating a held-aside (pilot) data set, fitting a prognostic score  
    (see Hansen (2008) <doi:10.1093/biomet/asn004>) on the pilot set, and stratifying the data set based
    on prognostic score quantiles.  The strata_match() function then does optimal
    matching of the data set in parallel within strata.
	"""
	
	homepage = "https://github.com/raikens1/stratamatch"
	cran = "stratamatch" 

	version("0.1.9", md5="3c96cbdbdbb2785b0930cda22504244b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-hmisc@4.2.0:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-survival@2.44.1.1:", type=("build", "run"))
