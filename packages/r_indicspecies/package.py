# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndicspecies(RPackage):
	"""Relationship Between Species and Groups of Sites

	Functions to assess the strength and statistical significance of the relationship between species occurrence/abundance and groups of sites [De Caceres & Legendre (2009) <doi:10.1890/08-1823.1>]. Also includes functions to measure species niche breadth using resource categories [De Caceres et al. (2011) <doi:10.1111/J.1600-0706.2011.19679.x>].
	"""
	
	homepage = "https://emf-creaf.github.io/indicspecies/"
	cran = "indicspecies" 

	version("1.7.14", md5="bd13e925225fa68d01bbaa380ffba954")

	depends_on("r-permute", type=("build", "run"))
