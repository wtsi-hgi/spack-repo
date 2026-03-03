# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeb(RPackage):
	"""A normalization-invariant minimum enclosing ball method to detect differentially expressed genes for RNA-seq and scRNA-seq data

	This package provides a method to identify differential expression genes in the same or different species. Given that non-DE genes have some similarities in features, a scaling-free minimum enclosing ball (SFMEB) model is built to cover those non-DE genes in feature space, then those DE genes, which are enormously different from non-DE genes, being regarded as outliers and rejected outside the ball. The method on this package is described in the article 'A minimum enclosing ball method to detect differential expression genes for RNA-seq data'. The SFMEB method is extended to the scMEB method that considering two or more potential types of cells or unknown labels scRNA-seq dataset DEGs identification.
	"""
	
	bioc = "MEB" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MEB_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MEB/MEB_1.16.0.tar.gz"]

	version("1.16.0", md5="b1785984524fee5b32976a5e768037d6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-wrswor", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
