# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunchip(RPackage):
	"""Clustering and Alignment of ChIP-Seq peaks based on their shapes

	Preprocessing and smoothing of ChIP-Seq peaks and efficient implementation of the k-mean alignment algorithm to classify them.
	"""
	
	bioc = "FunChIP" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/FunChIP_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/FunChIP/FunChIP_1.28.0.tar.gz"]

	version("1.28.0", md5="93a91487d2e6b0841094c9eb7c997be2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
