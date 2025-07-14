# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlogo2(RPackage):
	"""Plot Gene Ontology and KEGG pathway Annotation and Abundance

	Functions for enrichment analysis and plotting gene ontology or KEGG pathway information for multiple data subsets at the same time. It also enables encorporating multiple conditions and abundance data.
	"""
	
	bioc = "PloGO2"

	version("1.14.0", commit="d6bc3c948335d92daa51b11e6d5419df0b0a1e27")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
