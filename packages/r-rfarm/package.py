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

	version("1.20.0", commit="c82a20c7a6674397782ca89907156d84a7ef9bb3")
	version("1.14.2", commit="2714b9d8937ae602c94fd702720cb536e39413ff")

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
