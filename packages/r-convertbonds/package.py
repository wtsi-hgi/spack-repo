# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvertbonds(RPackage):
	"""Use the Given Parameters to Calculate the European Option Value

	Calculate the theoretical value of convertible bonds by given parameters, including B-S theory and Monte Carlo method.
	"""
	
	cran = "convertbonds" 

	version("0.1.0", md5="4224d72fd518f5d7905a83a8481eec17")

