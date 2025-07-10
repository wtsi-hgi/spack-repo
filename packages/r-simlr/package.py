# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimlr(RPackage):
	"""Single-cell Interpretation via Multi-kernel LeaRning (SIMLR)

	Single-cell RNA-seq technologies enable high throughput gene expression measurement of individual cells, and allow the discovery of heterogeneity within cell populations. Measurement of cell-to-cell gene expression similarity is critical for the identification, visualization and analysis of cell populations. However, single-cell data introduce challenges to conventional measures of gene expression similarity because of the high level of noise, outliers and dropouts. We develop a novel similarity-learning framework, SIMLR (Single-cell Interpretation via Multi-kernel LeaRning), which learns an appropriate distance metric from the data for dimension reduction, clustering and visualization.
	"""
	
	homepage = "https://github.com/BatzoglouLabSU/SIMLR"
	bioc = "SIMLR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SIMLR_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SIMLR/SIMLR_1.28.0.tar.gz"]

	version("1.28.0", sha256="5efb3a0248baf6b99728cdd2242b1ef437d4275dad8f43fa0e6e4854c1270ff2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcppannoy", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
