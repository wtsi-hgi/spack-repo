# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbtest(RPackage):
	"""Regression-Based Approach for Testing the Type of Missing Data

	The regression-based (RB) approach is a method to test the missing data mechanism.
			This package contains two functions that test the type of missing data (Missing Completely 
			At Random vs Missing At Random) on the basis of the RB approach. The first function applies 
			the RB approach independently on each variable with missing data, using the completely 
			observed variables only. The second function tests the missing data mechanism globally 
			(on all variables with missing data) with the use of all available information. The 
			algorithm is adapted both to continuous and categorical data. 
	"""
	
	cran = "RBtest" 

	version("1.1", md5="f486b45152dd8b103ddb889e0505f046")

	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
