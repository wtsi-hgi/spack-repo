# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovidsymptom(RPackage):
	"""COVID Symptom Study Sweden Open Dataset

	The COVID Symptom Study is a non-commercial project that uses a free mobile app to facilitate real-time data collection of symptoms, exposures, and risk factors related to COVID19. The package allows easy access to summary statistics data from COVID Symptom Study Sweden.
	"""
	
	homepage = "https://github.com/csss-resultat/covidsymptom"
	cran = "covidsymptom" 

	version("0.9.3", md5="9aaf509e39b4dd54101ff0f3a66ba627")

	depends_on("r@2.10:", type=("build", "run"))
