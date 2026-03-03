# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHindexcalculator(RPackage):
	"""H-Index Calculator using Data from a Web of Science (WoS)
Citation Report

	H(x) is the h-index for the past x years. Here, the h(x) of a scientist/department/etc. can be calculated using the exported excel file from a Web of Science citation report of a search. Also calculated is the year of first publication, total number of publications, and sum of times cited for the specified period. Therefore, for h-10: the date of first publication, total number of publications, and sum of times cited in the past 10 years are calculated. Note: the excel file has to first be saved in a .csv format.
	"""
	
	cran = "hindexcalculator" 

	version("1.0.0", md5="b2f4e95747d52d4de4cc1362a114bb68")

	depends_on("r@3.2:", type=("build", "run"))
