# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeanr(RPackage):
	"""Finds "Local Subnetworks" Within an Interaction Network which
Show Enrichment for Differentially Expressed Genes

	Implements the method described in "Network-based analysis of omics data: The LEAN method" [Gwinner Boulday (2016) <DOI:10.1093/bioinformatics/btw676>]
 Given a protein interaction network and a list of p-values describing a measure of interest (as e.g. differential gene expression) this method
 computes an enrichment p-value for the protein neighborhood of each gene and compares it to a background distribution of randomly drawn p-values.
 The resulting scores are corrected for multiple testing and significant hits are returned in tabular format.
	"""
	
	cran = "LEANR" 

	version("1.4.9", md5="3f98cb56394479cabb3a7c811c1bf6c0")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-igraph@0.7.1:", type=("build", "run"))
	depends_on("r-foreach@1.4.2:", type=("build", "run"))
