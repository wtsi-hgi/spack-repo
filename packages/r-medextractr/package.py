# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedextractr(RPackage):
	"""Extraction of Medication Information from Clinical Text

	Function and support for medication and dosing information extraction from free-text clinical notes. Medication entities for the basic medExtractR implementation that can be extracted include drug name, strength, dose amount, dose, frequency, intake time, dose change, and time of last dose. The basic medExtractR is outlined in Weeks, Beck, McNeer, Williams, Bejan, Denny, Choi (2020) <doi: 10.1093/jamia/ocz207>. The extended medExtractR_tapering implementation is intended to extract dosing information for more tapering schedules, which are far more complex. The tapering extension allows for the extraction of additional entities including dispense amount, refills, dose schedule, time keyword, transition, and preposition.
	"""
	
	cran = "medExtractR" 

	version("0.4.1", md5="65b936d8cd680cfd92b9ddcc25e28672")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
