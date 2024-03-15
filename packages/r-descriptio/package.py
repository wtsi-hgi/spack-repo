# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescriptio(RPackage):
	"""Descriptive Statistical Analysis

	Description of statistical associations between two variables : measures of local and global association between variables (phi, Cramér V, correlations, eta-squared, Goodman and Kruskal tau, permutation tests, etc.), multiple graphical representations of the associations between two variables (using 'ggplot2') and weighted statistics.
	"""
	
	homepage = "https://github.com/nicolas-robette/descriptio"
	cran = "descriptio" 

	version("1.3", md5="f1a05bcec54bcf6d027d32acf3f56a87")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
