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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PloGO2_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PloGO2/PloGO2_1.14.0.tar.gz"]

	version("1.14.0", md5="a9d28e5ed4822c97721db2c841ce3eec", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/PloGO2_1.14.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
