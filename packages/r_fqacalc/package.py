# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFqacalc(RPackage):
	"""Calculate Floristic Quality Assessment Metrics

	A collection of functions for calculating Floristic Quality
    Assessment (FQA) metrics using regional FQA databases that have been
    approved or approved with reservations as ecological planning models
    by the U.S. Army Corps of Engineers (USACE). For information on FQA
    see Spyreas (2019) <doi:10.1002/ecs2.2825>. These databases are stored
    in a sister R package, 'fqadata'. Both packages were developed for the
    USACE by the U.S. Army Engineer Research and Development Center’s
    Environmental Laboratory.
	"""
	
	cran = "fqacalc" 

	version("1.1.0", md5="cd9fd54b4c3dc2f7c45beac7ba71c79f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fqadata@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
