# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMreg(RPackage):
	"""Fits Regression Models When the Outcome is Partially Missing

	Implements the methods described in Bond S, Farewell V, 2006, Exact Likelihood Estimation for a Negative Binomial Regression Model with Missing Outcomes, Biometrics.
	"""
	
	homepage = "https://github.com/shug0131/mreg"
	cran = "mreg" 

	version("1.2.1", md5="ae4d6f9968eb5ef7eb3b7ad6ed802ffa")

