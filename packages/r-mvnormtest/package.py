# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnormtest(RPackage):
	"""Normality Test for Multivariate Variables

	Generalization of Shapiro-Wilk test for multivariate variables.
	"""
	
	cran = "mvnormtest" 

	version("0.1-9-3", md5="5040046e51bee05b6191e1abff06875d")

