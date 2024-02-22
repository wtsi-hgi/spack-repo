# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearningr(RPackage):
	"""Data and Functions to Accompany the Book "Learning R"

	Crabs in the English channel, deer skulls, English
    monarchs, half-caste Manga characters, Jamaican cities,
    Shakespeare's The Tempest, drugged up cyclists and sexually
    transmitted diseases.
	"""
	
	cran = "learningr" 

	version("0.29.1", md5="a3ba20f5c5d7045668b3d23d4550c698")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
