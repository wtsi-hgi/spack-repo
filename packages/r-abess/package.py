# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbess(RPackage):
	"""Fast Best Subset Selection

	Extremely efficient toolkit for solving the best subset selection problem <https://www.jmlr.org/papers/v23/21-1060.html>. This package is its R interface. The package implements and generalizes algorithms designed in <doi:10.1073/pnas.2014241117> that exploits a novel sequencing-and-splicing technique to guarantee exact support recovery and globally optimal solution in polynomial times for linear model. It also supports best subset selection for logistic regression, Poisson regression, Cox proportional hazard model, Gamma regression, multiple-response regression, multinomial logistic regression, ordinal regression, (sequential) principal component analysis, and robust principal component analysis. The other valuable features such as the best subset of group selection <doi:10.1287/ijoc.2022.1241> and sure independence screening <doi:10.1111/j.1467-9868.2008.00674.x> are also provided.  
	"""
	
	homepage = "https://github.com/abess-team/abess"
	cran = "abess" 

	version("0.4.8", md5="6712ac64335bbc2f99129e021b755752")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
