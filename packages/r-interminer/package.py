# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterminer(RPackage):
	"""R Interface with InterMine-Powered Databases

	Databases based on the InterMine platform such as FlyMine, modMine (modENCODE), RatMine, YeastMine, HumanMine and TargetMine are integrated databases of genomic, expression and protein data for various organisms. Integrating data makes it possible to run sophisticated data mining queries that span domains of biological knowledge. This R package provides interfaces with these databases through webservices. It makes most from the correspondence of the data frame object in R and the table object in databases, while hiding the details of data exchange through XML or JSON.
	"""
	
	bioc = "InterMineR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/InterMineR_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/InterMineR/InterMineR_1.24.0.tar.gz"]

	version("1.24.0", md5="a401e91084a8393592ceb3305b6cbfa2")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
