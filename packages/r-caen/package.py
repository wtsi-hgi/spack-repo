# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaen(RPackage):
	"""Category encoding method for selecting feature genes for the classification of single-cell RNA-seq

	With the development of high-throughput techniques, more and more gene expression analysis tend to replace hybridization-based microarrays with the revolutionary technology.The novel method encodes the category again by employing the rank of samples for each gene in each class. We then consider the correlation coefficient of gene and class with rank of sample and new rank of category. The highest correlation coefficient genes are considered as the feature genes which are most effective to classify the samples.
	"""
	
	bioc = "CAEN" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CAEN_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CAEN/CAEN_1.10.0.tar.gz"]

	version("1.10.0", md5="66decd595d2315a90c09b7d52df606c5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-poiclaclu", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
