# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcamethods(RPackage):
	"""A collection of PCA methods.

	Provides Bayesian PCA, Probabilistic PCA, Nipals PCA, Inverse Non-Linear
	PCA and the conventional SVD PCA. A cluster based method for missing
	value estimation is included for comparison. BPCA, PPCA and NipalsPCA
	may be used to perform PCA on incomplete data as well as for accurate
	missing value estimation. A set of methods for printing and plotting the
	results is also provided. All PCA methods make use of the same data
	structure (pcaRes) to provide a common interface to the PCA results.
	Initiated at the Max-Planck Institute for Molecular Plant Physiology,
	Golm, Germany."""

	bioc = "pcaMethods"

	license("GPL-2.0-or-later")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pcaMethods_1.94.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pcaMethods/pcaMethods_1.94.0.tar.gz"]

	version("1.94.0", md5="a989ad925a9852f55eb5e4d16d1529d0")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
