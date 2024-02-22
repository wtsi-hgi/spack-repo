# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFenr(RPackage):
	"""Fast functional enrichment for interactive applications

	Perform fast functional enrichment on feature lists (like genes or proteins) using the hypergeometric distribution. Tailored for speed, this package is ideal for interactive platforms such as Shiny. It supports the retrieval of functional data from sources like GO, KEGG, Reactome, Bioplanet and WikiPathways. By downloading and preparing data first, it allows for rapid successive tests on various feature selections without the need for repetitive, time-consuming preparatory steps typical of other packages.
	"""
	
	homepage = "https://github.com/bartongroup/fenr"
	bioc = "fenr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/fenr_1.0.5.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/fenr/fenr_1.0.5.tar.gz"]

	version("1.0.5", md5="7452c5f9c400c3a3a3af9a0b26e7585e")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
