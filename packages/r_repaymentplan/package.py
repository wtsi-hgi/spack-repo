# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepaymentplan(RPackage):
	"""Calculation of Mortgage Plan or Repayment Plan

	The function RepaymentPlan() calculates repayment schedule for repayment/mortgage plans.
	"""
	
	cran = "RepaymentPlan" 

	version("0.1.0", md5="3ff10118e6802e174ba88b895272d810")

