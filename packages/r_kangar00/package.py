# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKangar00(RPackage):
	"""Kernel Approaches for Nonlinear Genetic Association Regression

	Methods to extract information on pathways, genes and various single-nucleotid polymorphisms (SNPs) from online databases. It provides functions for data preparation and evaluation of genetic influence on a binary outcome using the logistic kernel machine test (LKMT). Three different kernel functions are offered to analyze genotype information in this variance component test: A linear kernel, a size-adjusted kernel and a network-based kernel (Friedrichs et al., 2017, <doi:10.1155/2017/6742763>).
	"""
	
	cran = "kangar00" 

	version("1.4.1", md5="4ee75558f03a03f64f1a767c727c37a0", url="https://cran.r-project.org/src/contrib/kangar00_1.4.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
