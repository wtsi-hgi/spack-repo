# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchfeat(RPackage):
	"""One-to-One Feature Matching

	Statistical methods to match feature vectors between multiple datasets in a one-to-one fashion. Given a fixed number of classes/distributions, for each unit, exactly one vector of each class is observed without label. The goal is to label the feature vectors using each label exactly once so to produce the best match across datasets, e.g. by minimizing the variability within classes. Statistical solutions based on empirical loss functions and probabilistic modeling are provided. The 'Gurobi' software and its 'R' interface package are required for one of the package functions (match.2x()) and can be obtained at <https://www.gurobi.com/> (free academic license). For more details, refer to Degras (2022) <doi:10.1080/10618600.2022.2074429> "Scalable feature matching for large data collections" and Bandelt, Maas, and Spieksma (2004) <doi:10.1057/palgrave.jors.2601723> "Local search heuristics for multi-index assignment problems with decomposable costs".
	"""
	
	cran = "matchFeat" 

	version("1.0", md5="58ba244adf08e8e9b0c977eeb3e467a6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
