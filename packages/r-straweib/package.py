# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStraweib(RPackage):
	"""Stratified Weibull Regression Model

	The main function is icweib(), which fits a stratified Weibull
    proportional hazards model for left censored, right censored, interval censored,
    and non-censored survival data. We parameterize the Weibull regression model
    so that it allows a stratum-specific baseline hazard function, but where the
    effects of other covariates are assumed to be constant across strata. 
    Please refer to Xiangdong Gu, David Shapiro, Michael D. Hughes and
    Raji Balasubramanian (2014) <doi:10.32614/RJ-2014-003> for more details.
	"""
	
	cran = "straweib" 

	version("1.1", md5="6e6ffc8e77c20d3bda939e0eb7b2d05e")

