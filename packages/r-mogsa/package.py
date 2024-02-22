# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogsa(RPackage):
	"""Multiple omics data integrative clustering and gene set analysis

	This package provide a method for doing gene set analysis based on multiple omics data.
	"""
	
	bioc = "mogsa" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mogsa_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mogsa/mogsa_1.36.0.tar.gz"]

	version("1.36.0", md5="177b003a38a7dc7ce3fb238369d1b6e7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
