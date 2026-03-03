# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynarankr(RPackage):
	"""Inferring Longitudinal Dominance Hierarchies

	Provides functions for inferring longitudinal dominance hierarchies, which describe dominance relationships and their dynamics in a single latent hierarchy over time. Strauss & Holekamp (in press). 
	"""
	
	homepage = "https://github.com/straussed/DynaRankR"
	cran = "DynaRankR" 

	version("1.1.0", md5="4bc89dc8307bb8eeef40c5739adb9715")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
