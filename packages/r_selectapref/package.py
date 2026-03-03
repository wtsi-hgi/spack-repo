# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectapref(RPackage):
	"""Analysis of Field and Laboratory Foraging

	Provides indices such as Manly's alpha, foraging ratio, and Ivlev's selectivity to allow for analysis of dietary selectivity and preference. Can accommodate multiple experimental designs such as constant prey number of prey depletion. Please contact the package maintainer with any publications making use of this package in an effort to maintain a repository of dietary selections studies.
	"""
	
	cran = "selectapref" 

	version("0.1.2", md5="86fc1bcb5e14773853b2835620fde76e")

	depends_on("r@3.2.3:", type=("build", "run"))
