# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnashaper(RPackage):
	"""High-throughput prediction of DNA shape features

	DNAhapeR is an R/BioConductor package for ultra-fast, high-throughput predictions of DNA shape features. The package allows to predict, visualize and encode DNA shape features for statistical learning.
	"""
	
	bioc = "DNAshapeR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DNAshapeR_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DNAshapeR/DNAshapeR_1.30.0.tar.gz"]

	version("1.30.0", md5="f2b90849d52bce75d88a4970f08c2544")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
