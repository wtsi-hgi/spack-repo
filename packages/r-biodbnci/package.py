# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbnci(RPackage):
	"""biodbNci, a library for connecting to biodbNci, a library for connecting to the National Cancer Institute (USA) CACTUS Database

	The biodbNci library is an extension of the biodb framework package. It provides access to biodbNci, a library for connecting to the National Cancer Institute (USA) CACTUS Database. It allows to retrieve entries by their accession number, and run specific web services.
	"""
	
	bioc = "biodbNci" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biodbNci_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biodbNci/biodbNci_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="5de583b026cc0ecbcf1983a9e8bbb72d7385e04dd2e61781c8dce8d907774db6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biodb@1.3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
