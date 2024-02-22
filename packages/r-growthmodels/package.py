# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowthmodels(RPackage):
	"""Nonlinear Growth Models

	A compilation of nonlinear growth models.
	"""
	
	homepage = "https://github.com/drodriguezperez/growthmodels"
	cran = "growthmodels" 

	version("1.3.1", md5="366d0a1cd23164b2b44518cc6d8b43fa")

