# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancerevolutionvisualization(RPackage):
	"""Publication Quality Phylogenetic Tree Plots

	Generates tree plots with precise branch lengths, gene annotations, and cellular prevalence. The package handles complex tree structures (angles, lengths, etc.) and can be further refined as needed by the user.
	"""
	
	homepage = "https://github.com/uclahs-cds/package-CancerEvolutionVisualization"
	cran = "CancerEvolutionVisualization" 

	version("2.0.1", md5="d7bc32e89d254cbf3eb7e6063200e0bb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-boutroslab-plotting-general", type=("build", "run"))
