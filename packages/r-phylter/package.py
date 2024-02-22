# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylter(RPackage):
	"""Detect and Remove Outliers in Phylogenomics Datasets

	Analyzis and filtering of phylogenomics datasets. 
	It takes an input either a collection of gene trees (then transformed to matrices) or directly a collection of gene matrices and performs an iterative process to identify
	what species in what genes are outliers, and whose elimination significantly improves the concordance between the input matrices. The methods builds upon the Distatis approach (Abdi et al. (2005) <doi:10.1101/2021.09.08.459421>), a generalization of classical multidimensional scaling to multiple distance matrices.
	"""
	
	cran = "phylter" 

	version("0.9.11", md5="95abaf1e9017a6959bfa6e04399ea3fe")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2.9:", type=("build", "run"))
	depends_on("r-rcpp@0.12.6:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
