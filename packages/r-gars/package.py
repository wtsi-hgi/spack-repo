# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGars(RPackage):
	"""GARS: Genetic Algorithm for the identification of Robust Subsets of variables in high-dimensional and challenging datasets

	Feature selection aims to identify and remove redundant, irrelevant and noisy variables from high-dimensional datasets. Selecting informative features affects the subsequent classification and regression analyses by improving their overall performances. Several methods have been proposed to perform feature selection: most of them relies on univariate statistics, correlation, entropy measurements or the usage of backward/forward regressions. Herein, we propose an efficient, robust and fast method that adopts stochastic optimization approaches for high-dimensional. GARS is an innovative implementation of a genetic algorithm that selects robust features in high-dimensional and challenging datasets.
	"""
	
	bioc = "GARS"

	version("1.28.0", commit="929d37057de99fa0f72851312ad60e280e216889")
	version("1.22.0", commit="acbc1279231ca8991c857db6c13d53562a08f232")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-damirseq", type=("build", "run"))
	depends_on("r-mlseq", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
