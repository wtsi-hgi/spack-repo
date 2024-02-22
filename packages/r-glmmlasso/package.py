# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmlasso(RPackage):
	"""Variable Selection for Generalized Linear Mixed Models by
L1-Penalized Estimation

	A variable selection approach for generalized linear mixed models by L1-penalized estimation is provided, 
	see Groll and Tutz (2014) <doi:10.1007/s11222-012-9359-z>.
	See also Groll and Tutz (2017) <doi:10.1007/s10985-016-9359-y> for discrete survival models including heterogeneity.
	"""
	
	cran = "glmmLasso" 

	version("1.6.3", md5="4496a290274dfaec8b997cfec9289a4c")

	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
