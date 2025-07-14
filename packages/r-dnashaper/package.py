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

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="d3d60db2d307ff6f5345f0ec3f7c46c41f17959056e51235ae1e0e6505fe8e4a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
