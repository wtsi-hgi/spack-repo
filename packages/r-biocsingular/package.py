# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocsingular(RPackage):
	"""Singular Value Decomposition for Bioconductor Packages.

	Implements exact and approximate methods for singular value
	decomposition and principal components analysis, in a framework that
	allows them to be easily switched within Bioconductor packages or
	workflows. Where possible, parallelization is achieved using the
	BiocParallel framework."""

	bioc = "BiocSingular"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiocSingular_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiocSingular/BiocSingular_1.18.0.tar.gz"]

	version("1.18.0", md5="9b4158e143f2cbefc140228c13090b35")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-scaledmatrix", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
