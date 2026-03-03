# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCat(RPackage):
	"""Analysis and Imputation of Categorical-Variable Datasets with
Missing Values

	Performs analysis of categorical-variable with missing values. Implements methods from Schafer, JL, Analysis of Incomplete Multivariate Data, Chapman and Hall.
	"""
	
	cran = "cat" 

	version("0.0-9", md5="40c1346caeddda9bb7c537b5adef0dba")

