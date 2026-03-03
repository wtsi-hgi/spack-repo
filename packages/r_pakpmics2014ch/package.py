# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPakpmics2014ch(RPackage):
	"""Multiple Indicator Cluster Survey (MICS) 2014 Child
Questionnaire Data for Punjab, Pakistan

	Provides data set and functions for exploration of Multiple Indicator Cluster Survey (MICS) 2014 Child questionnaire data for Punjab, Pakistan (<http://www.mics.unicef.org/surveys>).
	"""
	
	homepage = "https://github.com/MYaseen208/PakPMICS2014Ch"
	cran = "PakPMICS2014Ch" 

	version("0.1.0", md5="09f7de858b166af95b47636c09565315")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
