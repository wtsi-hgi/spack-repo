# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartcensreg(RPackage):
	"""Estimation and Diagnostics for Partially Linear Censored
Regression Models Based on Heavy-Tailed Distributions

	It estimates the parameters of a partially linear regression censored model via maximum penalized likelihood through of ECME algorithm. The model belong to the semiparametric class, that including a parametric and nonparametric component. The error term considered belongs to the scale-mixture of normal (SMN) distribution, that includes well-known heavy tails distributions as the Student-t distribution, among others. To examine the performance of the fitted model, case-deletion and local influence techniques are provided to show its robust aspect against outlying and influential observations. This work is based in Ferreira, C. S., & Paula, G. A. (2017) <doi:10.1080/02664763.2016.1267124> but considering the SMN family.
	"""
	
	cran = "PartCensReg" 

	version("1.39", md5="b18a9212fe3fcb790822c1e298f2a143")

	depends_on("r-ssym", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
