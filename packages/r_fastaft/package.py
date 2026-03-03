# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastaft(RPackage):
	"""Fast Regression for the Accelerated Failure Time (AFT) Model

	Fast censored linear regression for the accelerated failure time (AFT) model of Huang (2013) <doi:10.1111/sjos.12031>.
	"""
	
	cran = "fastAFT" 

	version("1.4", md5="0afbd7b5de267ad83e5c3161f9014e40")

	depends_on("r@2.8:", type=("build", "run"))
