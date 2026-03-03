# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBca1sg(RPackage):
	"""Block Coordinate Ascent with One-Step Generalized Rosen
Algorithm

	Implementing the Block Coordinate Ascent with One-Step Generalized Rosen (BCA1SG) algorithm on the semiparametric models for panel count data, interval-censored survival data, and degradation data. A comprehensive description of the BCA1SG algorithm can be found in Wang et al. (2020) <https://github.com/yudongstat/BCA1SG/blob/master/BCA1SG.pdf>. For details of the semiparametric models for panel count data, interval-censored survival data, and degradation data, please see Wellner and Zhang (2007) <doi:10.1214/009053607000000181>, Huang and Wellner (1997) <ISBN:978-0-387-94992-5>, and Wang and Xu (2010) <doi:10.1198/TECH.2009.08197>, respectively.
	"""
	
	cran = "BCA1SG" 

	version("0.1.0", md5="e565a64b362f43618caad36d0a91d488")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-logofgamma", type=("build", "run"))
