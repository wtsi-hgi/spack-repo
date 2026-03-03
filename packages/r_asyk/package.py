# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsyk(RPackage):
	"""Kernel Density Estimation

	A collection of functions related to density estimation by using Chen's (2000) idea. Mean Squared Errors (MSE) are calculated for estimated curves. For this purpose, R functions allow the distribution to be Gamma, Exponential or Weibull. For details see Chen (2000), Scaillet (2004) <doi:10.1080/10485250310001624819> and Khan and Akbar.
	"""
	
	homepage = "https://CRAN.R-project.org/package=AsyK"
	cran = "AsyK" 

	version("1.5.5", md5="3dcab9fb93b2d6a695d6ddff2a8b3450")

	depends_on("r-deltd", type=("build", "run"))
