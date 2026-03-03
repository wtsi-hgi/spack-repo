# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnearmtte(RPackage):
	"""One-Arm Clinical Trial Designs for Time-to-Event Endpoint

	Get operating characteristics of one-arm clinical trial designs for time-to-event endpoint through simulation and perform analysis with time-to-event data.
	"""
	
	cran = "OneArmTTE" 

	version("1.0", md5="341cb21dcfae54da0d22e98050e0b695")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
