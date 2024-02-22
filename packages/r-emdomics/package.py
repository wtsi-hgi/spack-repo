# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmdomics(RPackage):
	"""Earth Mover's Distance for Differential Analysis of Genomics Data

	The EMDomics algorithm is used to perform a supervised multi-class analysis to measure the magnitude and statistical significance of observed continuous genomics data between groups. Usually the data will be gene expression values from array-based or sequence-based experiments, but data from other types of experiments can also be analyzed (e.g. copy number variation). Traditional methods like Significance Analysis of Microarrays (SAM) and Linear Models for Microarray Data (LIMMA) use significance tests based on summary statistics (mean and standard deviation) of the distributions. This approach lacks power to identify expression differences between groups that show high levels of intra-group heterogeneity. The Earth Mover's Distance (EMD) algorithm instead computes the "work" needed to transform one distribution into another, thus providing a metric of the overall difference in shape between two distributions. Permutation of sample labels is used to generate q-values for the observed EMD scores. This package also incorporates the Komolgorov-Smirnov (K-S) test and the Cramer von Mises test (CVM), which are both common distribution comparison tests.
	"""
	
	bioc = "EMDomics" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/EMDomics_2.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/EMDomics/EMDomics_2.32.0.tar.gz"]

	version("2.32.0", md5="3ac097828648747f0be1ed4d956ecfa7")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-emdist", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cdft", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
