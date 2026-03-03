# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtraterrestrial(RPackage):
	"""Astrobiology Equations Estimating Extraterrestrial Life

	Finding life outside the planet Earth several is the ultimate goal of an astrobiologist. Using known astronomical measurements and assumptions the probability of extraterrestrial life existence could be estimated. Equations such as the Drake equation (1961) as stated in the paper of Molina (2019) <arXiv:1912.01783>, Seager (2013) <https://www.space.com/22648-drake-equation-alien-life-seager.html> and Foucher et al, (2017) <doi:10.3390/life7040040> are included in the 'extraterrestrial' package.
	"""
	
	cran = "extraterrestrial" 

	version("0.1.0", md5="53aac3f0366612214dca09fdcfffc882")

	depends_on("r@3.5:", type=("build", "run"))
