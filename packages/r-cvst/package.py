# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvst(RPackage):
	"""Fast Cross-Validation via Sequential Testing

	The fast cross-validation via sequential testing (CVST) procedure is an improved cross-validation procedure which uses non-parametric testing coupled with sequential analysis to determine the best parameter set on linearly increasing subsets of the data. By eliminating under-performing candidates quickly and keeping promising candidates as long as possible, the method speeds up the computation while preserving the capability of a full cross-validation. Additionally to the CVST the package contains an implementation of the ordinary k-fold cross-validation with a flexible and powerful set of helper objects and methods to handle the overall model selection process. The implementations of the Cochran's Q test with permutations and the sequential testing framework of Wald are generic and can therefore also be used in other contexts.
	"""
	
	cran = "CVST" 

	version("0.2-3", md5="08032c05dcea2d5ac36e119dcadca240")

	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
