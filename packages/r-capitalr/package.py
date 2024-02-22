# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCapitalr(RPackage):
	"""Capital Budgeting Analysis, Annuity Loan Calculations and
Amortization Schedules

	Provides Capital Budgeting Analysis functionality and the essential Annuity loan functions.
    Also computes Loan Amortization Schedules including schedules with irregular payments.
	"""
	
	cran = "capitalR" 

	version("1.3.0", md5="572e9437019ba451beb51b605dfc2a52")

