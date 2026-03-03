# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtbatchmarking(RPackage):
	"""Extended Batch Marking Models

	A system for batch-marking data analysis to estimate survival probabilities, capture probabilities, and enumerate the population abundance for both marked and unmarked individuals. The estimation of only marked individuals can be achieved through the batchMarkOptim() function. Similarly, the combined marked and unmarked can be achieved through the batchMarkUnmarkOptim() function. The algorithm was also implemented for the hidden Markov model encapsulated in batchMarkUnmarkOptim() to estimate the abundance of both marked and unmarked individuals in the population. The package is based on the paper: "Hidden Markov Models for Extended Batch Data" of Cowen et al. (2017) <doi:10.1111/biom.12701>.
	"""
	
	homepage = "https://github.com/Olobatuyi/extBatchMarking"
	cran = "extBatchMarking" 

	version("1.0.1", md5="34ca8266b05bd4d95a4c3b08911cfbb1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-optimbase", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
