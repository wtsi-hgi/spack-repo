# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylogr(RPackage):
	"""Functions for Phylogenetically Based Statistical Analyses

	Manipulation and analysis of phylogenetically simulated
        data sets and phylogenetically based analyses using GLS.
	"""
	
	homepage = "http://ligarto.org/rdiaz"
	cran = "PHYLOGR" 

	version("1.0.11", md5="ad9dea1539c693db751fa4ade19242ca")

	depends_on("r@1.8.1:", type=("build", "run"))
