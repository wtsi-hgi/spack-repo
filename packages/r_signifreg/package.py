# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignifreg(RPackage):
	"""Consistent Significance Controlled Variable Selection in
Generalized Linear Regression

	Provides significance controlled variable selection algorithms with different directions (forward, backward, stepwise) based on diverse criteria (AIC, BIC, adjusted r-square, PRESS, or p-value). The algorithm selects a final model with only significant variables defined as those with significant p-values after multiple testing correction such as Bonferroni, False Discovery Rate, etc. See Zambom and Kim (2018) <doi:10.1002/sta4.210>.
	"""
	
	cran = "SignifReg" 

	version("4.3", md5="17efda2027cf4f029eb88d45f1ada7cb")

	depends_on("r-car", type=("build", "run"))
