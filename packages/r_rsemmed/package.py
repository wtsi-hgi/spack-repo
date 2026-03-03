# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsemmed(RPackage):
	"""An interface to the Semantic MEDLINE database

	A programmatic interface to the Semantic MEDLINE database. It provides functions for searching the database for concepts and finding paths between concepts. Path searching can also be tailored to user specifications, such as placing restrictions on concept types and the type of link between concepts. It also provides functions for summarizing and visualizing those paths.
	"""
	
	homepage = "https://github.com/lmyint/rsemmed"
	bioc = "rsemmed" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rsemmed_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rsemmed/rsemmed_1.12.0.tar.gz"]

	version("1.12.0", md5="379f918582942443c9823373180a9978")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
