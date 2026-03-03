# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScore(RPackage):
	"""A Package to Score Behavioral Questionnaires

	Provides routines for scoring behavioral questionnaires. Includes scoring procedures for the 'International Physical Activity Questionnaire (IPAQ)' <http://www.ipaq.ki.se>. Compares physical functional performance to the age- and gender-specific normal ranges. 
	"""
	
	cran = "score" 

	version("1.0.2", md5="2ed41e5a10247918a6b038419c8c42ec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-msm@1.5:", type=("build", "run"))
