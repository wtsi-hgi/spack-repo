# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClogitlasso(RPackage):
	"""Sparse Conditional Logistic Regression for Matched Studies

	Fit a sequence of conditional logistic regression models with lasso, for small to large sized samples. Avalos, M., Pouyes, H., Grandvalet, Y., Orriols, L., & Lagarde, E. (2015) <doi:10.1186/1471-2105-16-S6-S1>.
	"""
	
	cran = "clogitLasso" 

	version("1.1", md5="a6d729840dba795b262920f69ce29ab1")

	depends_on("r-lassoshooting@0.1.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
