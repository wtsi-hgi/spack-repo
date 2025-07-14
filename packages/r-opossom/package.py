# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpossom(RPackage):
	"""Comprehensive analysis of transcriptome data

	This package translates microarray expression data into metadata of reduced dimension. It provides various sample-centered and group-centered visualizations, sample similarity analyses and functional enrichment analyses. The underlying SOM algorithm combines feature clustering, multidimensional scaling and dimension reduction, along with strong visualization capabilities. It enables extraction and description of functional expression modules inherent in the data.
	"""
	
	homepage = "http://som.izbi.uni-leipzig.de"
	bioc = "oposSOM" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/oposSOM_2.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/oposSOM/oposSOM_2.20.0.tar.gz"]

    version("2.26.0", tag="RELEASE_3_21")
	version("2.20.0", sha256="b2bb49c5cd340377d736cade144786bcc08290edff4f09dea4f847b2810a0c41")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("r-fastica", type=("build", "run"))
	depends_on("r-tsne", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-pixmap", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
