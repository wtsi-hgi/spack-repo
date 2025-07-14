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

	version("1.36.0", commit="b6ee88ffb138d3b8ddd212311bb19275ec4a22f8")
	version("1.30.0", commit="651bca96f9499c492c233886264121738f9a57d2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
