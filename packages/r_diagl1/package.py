# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiagl1(RPackage):
	"""Routines for Fit, Inference and Diagnostics in Linear L1 and LAD
Models

	Diagnostics for linear L1 regression (also known as LAD - Least Absolute Deviations), including: estimation, confidence intervals, tests of hypotheses, measures of leverage, methods of diagnostics for L1 regression, special diagnostics graphs and measures of leverage. The algorithms are based in Dielman (2005)  <doi:10.1080/0094965042000223680>, Elian et al. (2000) <doi:10.1080/03610920008832518> and Dodge (1997) <doi:10.1006/jmva.1997.1666>. This package builds on the 'quantreg' package, which is a well-established package for tuning quantile regression models. There are also tests to verify if the errors have a Laplace distribution based on the work of Puig and Stephens (2000) <doi:10.2307/1270952>.
	"""
	
	cran = "diagL1" 

	version("1.0.0", md5="d0de2e7d8f1e1865d90ef0cbdfdeb285", url="https://cran.r-project.org/src/contrib/diagL1_1.0.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quantreg@5.97:", type=("build", "run"))
	depends_on("r-greekletters@1.0.2:", type=("build", "run"))
	depends_on("r-conquer", type=("build", "run"))
	depends_on("r-lawstat", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
