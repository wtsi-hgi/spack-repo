# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcbiclust(RPackage):
	"""Massive correlating biclusters for gene expression data and associated methods

	Custom made algorithm and associated methods for finding, visualising and analysing biclusters in large gene expression data sets. Algorithm is based on with a supplied gene set of size n, finding the maximum strength correlation matrix containing m samples from the data set.
	"""
	
	bioc = "MCbiclust" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MCbiclust_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MCbiclust/MCbiclust_1.26.0.tar.gz"]

    version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="2b378b6293f5cd9bcf95c2ef1a539325415990ba04d64f6b458282d5a7a770c9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
