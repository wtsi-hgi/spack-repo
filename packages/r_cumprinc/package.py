# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCumprinc(RPackage):
	"""Functions Centered Around Microsoft Excel Cumprinc Function

	Provides similar functionality to 'Microsoft Excel' 'CUMPRINC' function <https://support.microsoft.com/en-us/office/cumprinc-function-94a4516d-bd65-41a1-bc16-053a6af4c04d>. 
    Returns principal remaining at a given month, principal paid in a month, and accumulated principal paid at a given month based on original loan amount, 
    monthly interest rate, and term of loan.
	"""
	
	cran = "cumprinc" 

	version("0.1", md5="57b6a1578847f7784933c281fb470d46")

