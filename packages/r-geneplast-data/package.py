# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneplastData(RPackage):
	"""Input data for the geneplast package via AnnotationHub

	The package geneplast.data provides datasets from different sources via AnnotationHub to use in geneplast pipelines. The datasets have species, phylogenetic trees, and orthology relationships among eukaryotes from different orthologs databases.
	"""
	
	bioc = "geneplast.data" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/geneplast.data_0.99.9.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/geneplast.data/geneplast.data_0.99.9.tar.gz"]

	version("0.99.9", sha256="1192673d63a98841285605a89bc75687a057378d77d0a48b49cf4d36499f61c4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-treeio", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-geneplast", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))

