# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPakpmics2014wm(RPackage):
	"""Multiple Indicator Cluster Survey (MICS) 2014 Women
Questionnaire Data for Punjab, Pakistan

	Provides data set and function for exploration of Multiple Indicator Cluster Survey 2014 Women (age 15-49 years) questionnaire data for Punjab, Pakistan.
	"""
	
	homepage = "https://github.com/MYaseen208/PakPMICS2014Wm"
	cran = "PakPMICS2014Wm" 

	version("0.1.1", md5="6bf63a415bd8a65b7638121f57820587")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
