# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlober(RPackage):
	"""Estimating Functions with Multivariate B-Splines

	Generalized LassO applied to knot selection in multivariate B-splinE Regression (GLOBER) implements a novel approach for estimating functions in a multivariate nonparametric regression model based on an adaptive knot selection for B-splines using the Generalized Lasso. For further details we refer the reader to the paper Savino, M. E. and Lévy-Leduc, C. (2023), <arXiv:2306.00686>.
	"""
	
	cran = "glober" 

	version("1.0", md5="5ffe245903826751475083b1627b00dc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genlasso", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
