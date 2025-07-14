# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndeed(RPackage):
	"""Interactive Visualization of Integrated Differential Expression and Differential Network Analysis for Biomarker Candidate Selection Package

	An R package for integrated differential expression and differential network analysis based on omic data for cancer biomarker discovery. Both correlation and partial correlation can be used to generate differential network to aid the traditional differential expression analysis to identify changes between biomolecules on both their expression and pairwise association levels. A detailed description of the methodology has been published in Methods journal (PMID: 27592383). An interactive visualization feature allows for the exploration and selection of candidate biomarkers.
	"""
	
	homepage = "http://github.com/ressomlab/INDEED"
	bioc = "INDEED"

	version("2.22.0", commit="1f92fcbd18a2794a268950c74444e0d206a708c3")
	version("2.16.0", commit="e36498b934349f76d979c696d491c2592938a43c")

	depends_on("r-glasso@1.8:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-devtools@1.13:", type=("build", "run"))
	depends_on("r-igraph@1.2.4:", type=("build", "run"))
	depends_on("r-visnetwork@2.0.6:", type=("build", "run"))
