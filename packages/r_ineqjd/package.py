# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIneqjd(RPackage):
	"""Inequality Joint Decomposition

	Computes and decomposes Gini, Bonferroni and Zenga 2007 point and synthetic concentration indexes. Decompositions are intended: by sources, by subpopulations and by sources and subpopulations jointly. References, Zenga M. M.(2007) <doi:10.1400/209575> Zenga M. (2015) <doi:10.1400/246627> Zenga M., Valli I. (2017) <doi:10.26350/999999_000005> Zenga M., Valli I. (2018) <doi:10.26350/999999_000011>. 
	"""
	
	cran = "ineqJD" 

	version("1.0", md5="448230e3f97e0e6632200699823c210b")

