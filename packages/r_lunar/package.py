# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLunar(RPackage):
	"""Calculate Lunar Phase & Distance, Seasons and Related
Environmental Factors

	Provides functions to calculate lunar and other related
    environmental covariates.
	"""
	
	cran = "lunar" 

	version("0.2-1", md5="ac4566ebe74430402face619a7229047")

	depends_on("r@2.10:", type=("build", "run"))
