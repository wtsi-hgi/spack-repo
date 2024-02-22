# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnormtest(RPackage):
	"""Normality test for multivariate variables

	Generalization of shapiro-wilk test for multivariate
        variables.
	"""
	
	cran = "mvnormtest" 

	version("0.1-9", md5="e5960fbfc0e69797eec01c16fe74ecb7")

