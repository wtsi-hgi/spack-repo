# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptivegpca(RPackage):
	"""Adaptive Generalized PCA

	Implements adaptive gPCA, as described in: Fukuyama, J. (2017)
    <arXiv:1702.00501>. The package also includes functionality for applying
    the method to 'phyloseq' objects so that the method can be easily applied
    to microbiome data and a 'shiny' app for interactive visualization. 
	"""
	
	cran = "adaptiveGPCA" 

	version("0.1.3", md5="6af2c95bff40027a7307107648372c88")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ape@3.1.4:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-phyloseq@1.14:", type=("build", "run"))
