# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthcal(RPackage):
	"""Health Calculator

	Health Calculator helps to find different parameters like basal metabolic rate, body mass index etc. related to fitness and health of a person.
	"""
	
	cran = "HealthCal" 

	version("0.1.1", md5="aaf76000996a6669e23585c02fe0deda")

