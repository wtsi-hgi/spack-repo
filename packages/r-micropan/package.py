# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicropan(RPackage):
	"""Microbial Pan-Genome Analysis

	A collection of functions for computations and visualizations of microbial pan-genomes.
	"""
	
	cran = "micropan" 

	version("2.1", md5="b11b17855c036fc9f1a2aa649b9c3215")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-microseq", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
