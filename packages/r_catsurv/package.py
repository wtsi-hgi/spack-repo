# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatsurv(RPackage):
	"""Computerized Adaptive Testing for Survey Research

	Provides methods of computerized adaptive testing for survey researchers.  See Montgomery and Rossiter (2020) <doi:10.1093/jssam/smz027>. Includes functionality for data fit with the classic item response methods including the latent trait model, Birnbaum`s three parameter model, the graded response, and the generalized partial credit model.  Additionally, includes several ability parameter estimation and item selection routines.  During item selection, all calculations are done in compiled C++ code.
	"""
	
	cran = "catSurv" 

	version("1.5.0", md5="72de194cf713f322417b65622c239a8c")

	depends_on("r-ltm@1.1.1:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp@1.0.1:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-bh@1.69.0.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppgsl@0.3.6:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
