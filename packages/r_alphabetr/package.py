# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphabetr(RPackage):
	"""Algorithms for High-Throughput Sequencing of Antigen-Specific T
Cells

	Provides algorithms for frequency-based pairing of alpha-beta T
  cell receptors.
	"""
	
	homepage = "http://github.com/edwardslee/alphabetr"
	cran = "alphabetr" 

	version("0.2.2", md5="0a3495adcaa32576f1da68452aed33cd")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-clue@0.3.50:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-multicool@0.1.9:", type=("build", "run"))
