# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeatseekr(RPackage):
	"""FeatSeekR an R package for unsupervised feature selection

	FeatSeekR performs unsupervised feature selection using replicated measurements. It iteratively selects features with the highest reproducibility across replicates, after projecting out those dimensions from the data that are spanned by the previously selected features. The selected a set of features has a high replicate reproducibility and a high degree of uniqueness.
	"""
	
	homepage = "https://github.com/tcapraz/FeatSeekR"
	bioc = "FeatSeekR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/FeatSeekR_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/FeatSeekR/FeatSeekR_1.2.0.tar.gz"]

    version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="4ead7a2139aca1f50d5d583edba32826ff1e19b1f4c0efa9c583dca58349b75b")

	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
