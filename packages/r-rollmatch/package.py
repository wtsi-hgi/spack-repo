# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRollmatch(RPackage):
	"""Rolling Entry Matching

	Functions to perform propensity score matching on rolling entry interventions for which a suitable "entry" date is not observed for nonparticipants. For more details, please reference Witman et al. (2018) <doi:10.1111/1475-6773.13086>.
	"""
	
	homepage = "https://github.com/RTIInternational/rollmatch"
	cran = "rollmatch" 

	version("2.0.3", md5="f777cde368fe152e231c7d6d57747394")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
