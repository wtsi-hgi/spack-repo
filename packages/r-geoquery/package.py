# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeoquery(RPackage):
	"""Get data from NCBI Gene Expression Omnibus (GEO).

	The NCBI Gene Expression Omnibus (GEO) is a public repository of
	microarray data. Given the rich and varied nature of this resource, it
	is only natural to want to apply BioConductor tools to these data.
	GEOquery is the bridge between GEO and BioConductor."""

	bioc = "GEOquery"

	license("MIT")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GEOquery_2.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GEOquery/GEOquery_2.70.0.tar.gz"]

	version("2.70.0", md5="5e8f233065ccb97c7cbb231479c936a0")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
