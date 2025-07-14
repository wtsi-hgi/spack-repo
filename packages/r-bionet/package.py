# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBionet(RPackage):
	"""Routines for the functional analysis of biological networks

	This package provides functions for the integrated analysis of protein-protein interaction networks and the detection of functional modules. Different datasets can be integrated into the network by assigning p-values of statistical tests to the nodes of the network. E.g. p-values obtained from the differential expression of the genes from an Affymetrix array are assigned to the nodes of the network. By fitting a beta-uniform mixture model and calculating scores from the p-values, overall scores of network regions can be calculated and an integer linear programming algorithm identifies the maximum scoring subnetwork.
	"""
	
	homepage = "http://bionet.bioapps.biozentrum.uni-wuerzburg.de/"
	bioc = "BioNet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BioNet_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BioNet/BioNet_1.62.0.tar.gz"]

	version("1.68.0", tag="RELEASE_3_21")
	version("1.62.0", sha256="78012ebdb0dc4acfbb179a1030b76a835617129b2bfb0ef34a3849f2b2915988")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
