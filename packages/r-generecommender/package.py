# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenerecommender(RPackage):
	"""A gene recommender algorithm to identify genes coexpressed with a query set of genes

	This package contains a targeted clustering algorithm for the analysis of microarray data. The algorithm can aid in the discovery of new genes with similar functions to a given list of genes already known to have closely related functions.
	"""
	
	bioc = "geneRecommender" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/geneRecommender_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/geneRecommender/geneRecommender_1.74.0.tar.gz"]

	version("1.74.0", sha256="89202dd62cb18ff0a577ec8d38f72206d30ddaf90e39a1fecc8fa446399efef2")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
