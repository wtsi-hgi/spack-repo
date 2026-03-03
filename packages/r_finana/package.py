# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinana(RPackage):
	"""Financial Analysis and Regression Diagnostic Analysis

	Functions for financial analysis and financial modeling, 
             including batch graphs generation, beta calculation, 
             descriptive statistics, annuity calculation, bond pricing 
             and financial data download.
	"""
	
	cran = "FinAna" 

	version("0.1.2", md5="ebda3bcca5bf40a509d7ef37f5b82917")

