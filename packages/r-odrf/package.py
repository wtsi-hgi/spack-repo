# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdrf(RPackage):
	"""Oblique Decision Random Forest for Classification and Regression

	The oblique decision tree (ODT) uses linear combinations of
    predictors as partitioning variables in a decision tree. Oblique
    Decision Random Forest (ODRF) is an ensemble of multiple ODTs
    generated by feature bagging. Both can be used for classification and
    regression as supplements to the classical CART of Breiman (1984)
    <DOI:10.1201/9781315139470> and Random Forest of Breiman (2001)
    <DOI:10.1023/A:1010933404324> respectively.
	"""
	
	homepage = "https://liuyu-star.github.io/ODRF/"
	cran = "ODRF" 

	version("0.0.4", md5="a7501dfbd39c440d0a1c3a752f7b0ed6")

	depends_on("r-partykit", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pursuit", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
