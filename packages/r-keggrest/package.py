# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeggrest(RPackage):
	"""Client-side REST access to KEGG.

	A package that provides a client interface to the KEGG REST server.
	Based on KEGGSOAP by J. Zhang, R. Gentleman, and Marc Carlson, and KEGG
	(python package) by Aurelien Mazurie."""

	bioc = "KEGGREST"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/KEGGREST_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/KEGGREST/KEGGREST_1.42.0.tar.gz"]

	version("1.42.0", md5="805cb8808b0ffa6f57999b880337b504")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
