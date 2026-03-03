# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLjr(RPackage):
	"""Logistic Joinpoint Regression

	Fits and tests logistic joinpoint models.
	"""
	
	cran = "ljr" 

	version("1.4-0", md5="f0f31e45f01e5b2cb66e053cac734bd5")

