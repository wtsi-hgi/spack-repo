# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissonet(RPackage):
	"""Missingness in Multi-Task Regression with Network Estimation

	Efficient procedures for fitting conditional graphical lasso
    models that link a set of predictor variables to a set of response
    variables (or tasks), even when the response data may contain missing
    values. 'missoNet' simultaneously estimates the predictor
    coefficients for all tasks by leveraging information from one another,
    in order to provide more accurate predictions in comparison to
    modeling them individually. Additionally, 'missoNet' estimates the
    response network structure influenced by conditioning predictor
    variables using a L1-regularized conditional Gaussian graphical model.
    Unlike most penalized multi-task regression methods (e.g., MRCE),
    'missoNet' is capable of obtaining estimates even when the response
    data is corrupted by missing values. The method automatically enjoys
    the theoretical and computational benefits of convexity, and returns
    solutions that are comparable to the estimates obtained without
    missingness.
	"""
	
	homepage = "https://github.com/yixiao-zeng/missoNet"
	cran = "missoNet" 

	version("1.2.0", md5="37172dc50a7866222d4f6a8877df32b6")

	depends_on("r-circlize@0.4.14:", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-glasso@1.11:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.3:", type=("build", "run"))
	depends_on("r-pbapply@1.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scatterplot3d@0.3.41:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
