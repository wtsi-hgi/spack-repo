# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFella(RPackage):
	"""Interpretation and enrichment for metabolomics data

	Enrichment of metabolomics data using KEGG entries. Given a set of affected compounds, FELLA suggests affected reactions, enzymes, modules and pathways using label propagation in a knowledge model network. The resulting subnetwork can be visualised and exported.
	"""
	
	bioc = "FELLA"

	version("1.28.0", commit="9037a05ea768b97c3e974423d72fcefff8c8a56f")
	version("1.22.0", commit="3444f450f741e78e36fc080193a7298a97482a99")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
