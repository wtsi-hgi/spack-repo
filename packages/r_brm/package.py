# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrm(RPackage):
	"""Binary Regression Model

	Fits novel models for the conditional relative risk, risk difference and odds ratio <doi:10.1080/01621459.2016.1192546>.
	"""
	
	homepage = "http://github.com/mclements/brm"
	cran = "brm" 

	version("1.1.1", md5="0a7eae262f3e2b390d8894a3feb890cf")

