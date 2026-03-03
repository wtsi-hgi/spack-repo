# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdd(RPackage):
	"""Mixture modeling of single-cell RNA-seq data to identify genes with differential distributions

	This package implements a method to analyze single-cell RNA- seq Data utilizing flexible Dirichlet Process mixture models. Genes with differential distributions of expression are classified into several interesting patterns of differences between two conditions. The package also includes functions for simulating data with these patterns from negative binomial distributions.
	"""
	
	homepage = "https://github.com/kdkorthauer/scDD"
	bioc = "scDD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scDD_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scDD/scDD_1.26.0.tar.gz"]

	version("1.26.0", md5="3c95209683b09f0584ab315a6fc1e779")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-outliers", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ebseq", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
