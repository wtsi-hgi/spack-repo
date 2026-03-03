# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHospitals(RPackage):
	"""Portuguese 'NHS' Hospitals

	A data set of the Portuguese 'NHS' hospitals.
	"""
	
	homepage = "https://github.com/nhs-pt/hospitals"
	cran = "hospitals" 

	version("0.1.0", md5="0dad285185a0efce4adbff5a3302d643")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
