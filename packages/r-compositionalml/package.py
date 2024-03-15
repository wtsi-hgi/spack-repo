# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompositionalml(RPackage):
	"""Machine Learning with Compositional Data

	Machine learning algorithms for predictor variables that are compositional data and the response variable is either continuous or categorical. Specifically, the Boruta variable selection algorithm, random forest, support vector machines and projection pursuit regression are included. Relevant papers include: Tsagris M.T., Preston S. and Wood A.T.A. (2011). "A data-based power transformation for compositional data". Fourth International International Workshop on Compositional Data Analysis. <doi:10.48550/arXiv.1106.1451> and Alenazi, A. (2023). "A review of compositional data analysis and recent advances". Communications in Statistics--Theory and Methods, 52(16): 5535--5567. <doi:10.1080/03610926.2021.2014890>.
	"""
	
	cran = "CompositionalML" 

	version("1.0", md5="dd425c68441a20346d18cae19301ed2d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-boruta", type=("build", "run"))
	depends_on("r-compositional", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
