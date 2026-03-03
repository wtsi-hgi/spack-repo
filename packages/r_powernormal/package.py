# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowernormal(RPackage):
	"""Power Normal Distribution

	Miscellaneous functions for a descriptive analysis and initial Bayesian and classical 
             inference for the power parameter of the the Power Normal (PN) distribution. This 
             miscellaneous will be extend for more distributions into the power family and the 
             three-parameter model.
	"""
	
	cran = "PowerNormal" 

	version("1.2.0", md5="4049f867c844f743ec729fd65673491e")

