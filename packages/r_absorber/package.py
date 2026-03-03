# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbsorber(RPackage):
	"""Variable Selection in Nonparametric Models using B-Splines

	A variable selection method using B-Splines in multivariate nOnparametric Regression models Based on partial dErivatives Regularization (ABSORBER) implements a novel variable selection method in a nonlinear multivariate model using B-splines. For further details we refer the reader to the paper Savino, M. E. and Lévy-Leduc, C. (2024), <https://hal.science/hal-04434820>.
	"""
	
	cran = "absorber" 

	version("1.0", md5="f4c2843843dbaf6f519427c0b1e168db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsegl", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
