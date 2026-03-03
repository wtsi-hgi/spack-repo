# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpese(RPackage):
	"""Estimates of Standard Errors for Risk and Performance Measures

	Estimates of standard errors of popular risk and performance 
             measures for asset or portfolio returns using methods as described in 
             Chen and Martin (2021) <doi:10.21314/JOR.2020.446>.
	"""
	
	cran = "RPESE" 

	version("1.2.5", md5="436aa6c741ebeff4a9ecab7d5a1685e8")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rpeif", type=("build", "run"))
	depends_on("r-rpeglmen", type=("build", "run"))
	depends_on("r-robstattm", type=("build", "run"))
