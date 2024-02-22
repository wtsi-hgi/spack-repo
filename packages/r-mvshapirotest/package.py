# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvshapirotest(RPackage):
	"""Generalized Shapiro-Wilk test for multivariate normality

	This package implements the generalization of the Shapiro-Wilk test
        for multivariate normality proposed by Villasenor-Alva and
        Gonzalez-Estrada (2009).
	"""
	
	cran = "mvShapiroTest" 

	version("1.0", md5="b0098814d73d98b7d66a3eb3932e30f0")

