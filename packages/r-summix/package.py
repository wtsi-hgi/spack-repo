# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummix(RPackage):
	"""Summix: A method to estimate and adjust for population structure in genetic summary data

	This package contains the Summix method for estimating and adjusting for ancestry in genetic summary allele frequency data. The function summix estimates reference ancestry proportions using a mixture model. The adjAF function produces ancestry adjusted allele frequencies for an observed sample with ancestry proportions matching a target person or sample.
	"""
	
	bioc = "Summix"

	version("2.14.0", commit="9a2ca603ee3d62321f157543d8a22d40d26f843f")
	version("2.8.0", commit="1bae552a19d3a567eb41c02dff1b80be54e7df8c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
