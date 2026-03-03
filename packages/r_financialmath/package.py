# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinancialmath(RPackage):
	"""Financial Mathematics for Actuaries

	Contains financial math functions and introductory derivative functions included in the Society of Actuaries and Casualty Actuarial Society 'Financial Mathematics' exam, and some topics in the 'Models for Financial Economics' exam.
	"""
	
	cran = "FinancialMath" 

	version("0.1.1", md5="909ea72771262927bd349b5b716b03b4")

