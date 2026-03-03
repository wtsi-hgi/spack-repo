# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPakpmics2014hl(RPackage):
	"""Multiple Indicator Cluster Survey (MICS) 2014 Household Listing
Questionnaire Data for Punjab, Pakistan

	Provides data set and function for exploration of Multiple Indicator Cluster Survey 2014 Household Listing questionnaire data for Punjab, Pakistan.
	"""
	
	homepage = "https://github.com/MYaseen208/PakPMICS2014HL"
	cran = "PakPMICS2014HL" 

	version("0.1.1", md5="1d68dc38d2dc2d2422db58d2b744afe5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
