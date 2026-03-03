# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordofmouth(RPackage):
	"""Estimates Economic Variables for Word-of-Mouth-Campaigns

	Methods for estimating profit, profit-maximizing price, demand and consumer surplus of Word-of-Mouth-campaigns on mean-field networks.
	"""
	
	cran = "WordOfMouth" 

	version("1.1.0", md5="e354fb4edb51b742e41e25c942809d56")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-lambertw", type=("build", "run"))
