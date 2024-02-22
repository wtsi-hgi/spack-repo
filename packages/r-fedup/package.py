# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFedup(RPackage):
	"""Fisher's Test for Enrichment and Depletion of User-Defined Pathways

	An R package that tests for enrichment and depletion of user-defined pathways using a Fisher's exact test. The method is designed for versatile pathway annotation formats (eg. gmt, txt, xlsx) to allow the user to run pathway analysis on custom annotations. This package is also integrated with Cytoscape to provide network-based pathway visualization that enhances the interpretability of the results.
	"""
	
	homepage = "https://github.com/rosscm/fedup"
	bioc = "fedup" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/fedup_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/fedup/fedup_1.10.0.tar.gz"]

	version("1.10.0", md5="a5ac34da42c1a460ab50e307c73f8116")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
