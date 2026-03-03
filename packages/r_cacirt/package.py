# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCacirt(RPackage):
	"""Classification Accuracy and Consistency under Item Response
Theory

	Computes classification accuracy and consistency indices under Item Response Theory. Implements the total score IRT-based methods in Lee, Hanson & Brennen (2002) and Lee (2010), the IRT-based methods in Rudner (2001, 2005), and the total score nonparametric methods in Lathrop & Cheng (2014). For dichotomous and polytomous tests.
	"""
	
	cran = "cacIRT" 

	version("1.4", md5="4013a70aaa23567a4451ca84b8c7b7d1")

