# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsdr(RPackage):
	"""Differential gene co-expression

	This package contains functionality to run differential gene co-expression across two different conditions. The algorithm is inspired by Voigt et al. 2017 and finds Conserved, Specific and Differentiated genes (hence the name CSD). This package include efficient and variance calculation by bootstrapping and Welford's algorithm.
	"""
	
	homepage = "https://almaaslab.github.io/csdR"
	bioc = "csdR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/csdR_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/csdR/csdR_1.8.0.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="704fc3b7d90557f3dd5c13c72d20f99956a6e4757a9b53a9f0bbdf7aa403e4e6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
