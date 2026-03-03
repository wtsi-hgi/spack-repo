# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmdbquery(RPackage):
	"""utilities for exploration of human metabolome database

	Define utilities for exploration of human metabolome database, including functions to retrieve specific metabolite entries and data snapshots with pairwise associations (metabolite-gene,-protein,-disease).
	"""
	
	bioc = "hmdbQuery" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hmdbQuery_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hmdbQuery/hmdbQuery_1.22.0.tar.gz"]

	version("1.22.0", md5="32b8de26d3b369730bdd7c734da1be06")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
