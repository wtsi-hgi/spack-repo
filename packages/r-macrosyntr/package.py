# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacrosyntr(RPackage):
	"""Draw Ordered Oxford Grids and Chord Diagrams

	Use standard genomics file format (BED) and a table of orthologs to 
 illustrate synteny conservation at the genome-wide scale. 
 Significantly conserved linkage groups are identified as described in Simakov et al. (2020) <doi:10.1038/s41559-020-1156-z> 
 and displayed on an Oxford Grid (Edwards (1991) <doi:10.1111/j.1469-1809.1991.tb00394.x>) or a chord diagram as in Simakov et al. (2022) <doi:10.1126/sciadv.abi5884>. 
 The package provides a function that uses a network-based greedy algorithm to find communities (Clauset et al. (2004) <doi:10.1103/PhysRevE.70.066111>) 
 and so automatically order the chromosomes on the plot to improve interpretability.
	"""
	
	homepage = "https://github.com/SamiLhll/macrosyntR"
	cran = "macrosyntR" 

	version("0.3.3", md5="698620985f91704f9624521a043df0a3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
