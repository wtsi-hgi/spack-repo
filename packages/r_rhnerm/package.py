# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhnerm(RPackage):
	"""Random Heteroscedastic Nested Error Regression

	Performs the random heteroscedastic nested error regression model described in Kubokawa, Sugasawa, Ghosh and Chaudhuri (2016) <doi:10.5705/ss.202014.0070>.
	"""
	
	cran = "rhnerm" 

	version("1.1", md5="425b8fe7eacb9f29c64ea7b30287ded7")

