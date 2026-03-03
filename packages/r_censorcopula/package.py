# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensorcopula(RPackage):
	"""Estimate Parameter of Bivariate Copula

	Implement an interval censor method 
 to break ties when using data with ties to fitting a 
 bivariate copula.
	"""
	
	cran = "censorcopula" 

	version("2.0", md5="5790f6da1676700c6d31607f4942fdf0")

	depends_on("r-copula", type=("build", "run"))
