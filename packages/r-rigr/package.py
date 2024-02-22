# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRigr(RPackage):
	"""Regression, Inference, and General Data Analysis Tools in R

	A set of tools to streamline data analysis. Learning both R and introductory statistics at the same time can be challenging, and so we created 'rigr' to facilitate common data analysis tasks and enable learners to focus on statistical concepts. We provide easy-to-use interfaces for descriptive statistics, one- and two-sample inference, and regression analyses. 'rigr' output includes key information while omitting unnecessary details that can be confusing to beginners. Heteroscedasticity-robust ("sandwich") standard errors are returned by default, and multiple partial F-tests and tests for contrasts are easy to specify. A single regression function can fit both linear and generalized linear models, allowing students to more easily make connections between different classes of models.
	"""
	
	homepage = "https://statdivlab.github.io/rigr/"
	cran = "rigr" 

	version("1.0.4", md5="bf0ce93919bca8c16f7e6218cdb79c59")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
