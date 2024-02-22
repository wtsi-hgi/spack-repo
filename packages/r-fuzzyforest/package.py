# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyforest(RPackage):
	"""Fuzzy Forests

	Fuzzy forests, a new algorithm based on random forests,
    is designed to reduce the bias seen in random forest feature selection
    caused by the presence of correlated features.  Fuzzy forests uses
    recursive feature elimination random forests to select
    features from separate blocks of correlated features where the
    correlation within each block of features is high
    and the correlation between blocks of features is low.
    One final random forest is fit using the surviving features.
    This package fits random forests using the 'randomForest' package and
    allows for easy use of 'WGCNA' to split features into distinct blocks.
    See D. Conn, Ngun, T., C. Ramirez, and G. Li (2019) <doi:10.18637/jss.v091.i09>
    for further details.
	"""
	
	cran = "fuzzyforest" 

	version("1.0.8", md5="69556c7912a9ae21e8412d08d4d4ef2e")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
