# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPairwise(RPackage):
	"""Rasch Model Parameters by Pairwise Algorithm

	Performs the explicit calculation
    -- not estimation! -- of the Rasch item parameters for dichotomous and
    polytomous item responses, using a pairwise comparison approach. Person
    parameters (WLE) are calculated according to Warm's weighted likelihood
    approach.
	"""
	
	cran = "pairwise" 

	version("0.6.1-0", md5="27ad9071c89745ec97c2fe09c152a044")

	depends_on("r@3.5:", type=("build", "run"))
