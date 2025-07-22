# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenegeneinter(RPackage):
	"""Tools for Testing Gene-Gene Interaction at the Gene Level

	The aim of this package is to propose several methods for testing gene-gene interaction in case-control association studies. Such a test can be done by aggregating SNP-SNP interaction tests performed at the SNP level (SSI) or by using gene-gene multidimensionnal methods (GGI) methods. The package also proposes tools for a graphic display of the results. <doi:10.18637/jss.v095.i12>.
	"""
	
	bioc = "GeneGeneInteR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeneGeneInteR_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeneGeneInteR/GeneGeneInteR_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="fe6fea77a026faa323539d5e485cd7d2e4b07247d2b6b1bc6d0dd8c5503cdfad")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
