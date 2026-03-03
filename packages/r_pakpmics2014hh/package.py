# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPakpmics2014hh(RPackage):
	"""Multiple Indicator Cluster Survey (MICS) 2014 Household
Questionnaire Data for Punjab, Pakistan

	Provides data set and function for exploration of Multiple Indicator Cluster Survey (MICS) 2014 Household questionnaire data for Punjab, Pakistan (<http://www.mics.unicef.org/surveys>).
	"""
	
	homepage = "https://github.com/MYaseen208/PakPMICS2014HH"
	cran = "PakPMICS2014HH" 

	version("0.1.0", md5="4609c9e0fb479b856daf24b84e810f97")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
