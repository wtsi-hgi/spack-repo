# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugprepr(RPackage):
	"""Prepare Electronic Prescription Record Data to Estimate Drug
Exposure

	Prepare prescription data (such as from the Clinical Practice Research Datalink) into an analysis-ready format, with start and stop dates for each patient's prescriptions. Based on Pye et al (2018) <doi:10.1002/pds.4440>.
	"""
	
	cran = "drugprepr" 

	version("0.0.4", md5="943766bc34d20c24ac2a944bbd0012cb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doseminer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
