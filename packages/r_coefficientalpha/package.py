# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoefficientalpha(RPackage):
	"""Robust Coefficient Alpha and Omega with Missing and Non-Normal
Data

	Cronbach's alpha and McDonald's omega are widely used reliability or internal consistency measures in social, behavioral and education sciences. Alpha is reported in nearly every study that involves measuring a construct through multiple test items. The package 'coefficientalpha' calculates coefficient alpha and coefficient omega with missing data and non-normal data. Robust standard errors and confidence intervals are also provided. A test is also available to test the tau-equivalent and homogeneous assumptions. Since Version 0.5, the bootstrap confidence intervals were added.
	"""
	
	cran = "coefficientalpha" 

	version("0.7.2", md5="6c12959b0ea73a5fda5391ec22e2c150")

	depends_on("r-rsem", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
