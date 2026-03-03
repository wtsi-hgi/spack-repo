# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmomrfa(RPackage):
	"""Regional Frequency Analysis using L-Moments

	Functions for regional frequency analysis using the methods
  of J. R. M. Hosking and J. R. Wallis (1997), "Regional frequency analysis:
  an approach based on L-moments".
	"""
	
	cran = "lmomRFA" 

	version("3.6", md5="ea10b6908a5cd8ee03b31ed20eaf8ca8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lmom@2:", type=("build", "run"))
