# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCequre(RPackage):
	"""Censored Quantile Regression & Monotonicity-Respecting Restoring

	Perform censored quantile regression of Huang (2010) <doi:10.1214/09-AOS771>, and restore monotonicity respecting via adaptive interpolation for dynamic regression of Huang (2017) <doi:10.1080/01621459.2016.1149070>. The monotonicity-respecting restoration applies to general dynamic regression models including (uncensored or censored) quantile regression model, additive hazards model, and dynamic survival models of Peng and Huang (2007) <doi:10.1093/biomet/asm058>, among others.
	"""
	
	cran = "cequre" 

	version("1.5", md5="79eabc82edce8e13c7944c472d6fc6bf")

	depends_on("r@2.8:", type=("build", "run"))
