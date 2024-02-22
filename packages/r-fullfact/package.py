# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFullfact(RPackage):
	"""Full Factorial Breeding Analysis

	We facilitate the analysis of full factorial mating designs with mixed-effects models. The package contains six vignettes containing detailed examples.
	"""
	
	cran = "fullfact" 

	version("1.5.2", md5="28c5783191542adec88a1767dda219f4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-afex", type=("build", "run"))
