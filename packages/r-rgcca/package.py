# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgcca(RPackage):
	"""Regularized and Sparse Generalized Canonical Correlation
Analysis for Multiblock Data

	Multi-block data analysis concerns the analysis of several
    sets of variables (blocks) observed on the same group of individuals.
    The main aims of the RGCCA package are: to study the relationships
    between blocks and to identify subsets of variables of each block
    which are active in their relationships with the other blocks. This
    package allows to (i) run R/SGCCA and related methods,
    (ii) help the user to find out the optimal parameters for R/SGCCA such
    as regularization parameters (tau or sparsity), (iii) evaluate the
    stability of the RGCCA results and their significance, (iv) build predictive
    models from the R/SGCCA. (v) Generic print()
    and plot() functions apply to all these functionalities.
	"""
	
	homepage = "https://github.com/rgcca-factory/RGCCA"
	cran = "RGCCA" 

	version("3.0.3", md5="512c9cb809957a51a28716bb413162d0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
