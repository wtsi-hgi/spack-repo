# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfarm(RPackage):
	"""An R interface to the Rfam database

	rfaRm provides a client interface to the Rfam database of RNA families. Data that can be retrieved include RNA families, secondary structure images, covariance models, sequences within each family, alignments leading to the identification of a family and secondary structures in the dot-bracket format.
	"""
	
	bioc = "rfaRm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rfaRm_1.14.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rfaRm/rfaRm_1.14.2.tar.gz"]

	version("1.14.2", sha256="6b953d538843e8e4b4d0cc8b324b844096be065265277c279b51876ae2f1395e")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
