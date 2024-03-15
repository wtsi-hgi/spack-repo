# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomvrcns(RPackage):
	"""Copy Number study and Segmentation for multivariate biological data

	In this package, a Hidden Semi Markov Model (HSMM) and one homogeneous segmentation model are designed and implemented for segmentation genomic data, with the aim of assisting in transcripts detection using high throughput technology like RNA-seq or tiling array, and copy number analysis using aCGH or sequencing.
	"""
	
	bioc = "biomvRCNS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biomvRCNS_1.42.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biomvRCNS/biomvRCNS_1.42.2.tar.gz"]

	version("1.42.2", md5="48d65764f6fb51d742e578d18417a1b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
