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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/FELLA_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/FELLA/FELLA_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="e224c04e3702d64e67f0b3ab5ee98190263827c1d5dda6b51fb0bbb3fdd9b236")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
