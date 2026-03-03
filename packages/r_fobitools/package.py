# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFobitools(RPackage):
	"""Tools For Manipulating FOBI Ontology

	A set of tools for interacting with Food-Biomarker Ontology (FOBI). A collection of basic manipulation tools for biological significance analysis, graphs, and text mining strategies for annotating nutritional data.
	"""
	
	homepage = "https://github.com/pcastellanoescuder/fobitools/"
	bioc = "fobitools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fobitools_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fobitools/fobitools_1.10.0.tar.gz"]

	version("1.10.0", md5="24ebda3aed06055ab55d7cdf88a7c2a0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-recordlinkage", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-textclean", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
