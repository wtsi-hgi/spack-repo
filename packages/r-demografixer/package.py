# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemografixer(RPackage):
	"""Extrapolate Gender, Age and Nationality of a Name

	Connects to the <https://genderize.io/>, <https://agify.io/> and <https://nationalize.io/> APIs to estimate gender, age and nationality of a first name.
	"""
	
	homepage = "https://matbmeijer.github.io/DemografixeR"
	cran = "DemografixeR" 

	version("0.1.1", md5="8046943b4e90c712f5189ae23683f86f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
