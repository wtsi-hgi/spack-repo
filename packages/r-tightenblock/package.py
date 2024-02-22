# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTightenblock(RPackage):
	"""Tightens an Observational Block Design by Balanced Subset
Matching

	Tightens an observational block design into a smaller design with either smaller or fewer blocks while controlling for covariates. The method uses fine balance, optimal subset matching (Rosenbaum, 2012 <doi:10.1198/jcgs.2011.09219>) and two-criteria matching (Zhang et al 2023 <doi:10.1080/01621459.2021.1981337>).  The main function is tighten().  The suggested 'rrelaxiv' package for solving minimum cost flow problems: (i) derives from Bertsekas and Tseng (1988) <doi:10.1007/BF02288322>, (ii) is not available on CRAN due to its academic license, (iii) may be downloaded from GitHub at <https://github.com/josherrickson/rrelaxiv/>, (iv) is not essential to use the package.
	"""
	
	cran = "tightenBlock" 

	version("0.1.7", md5="13d0a19ed1f60d9628d74476d6bfd738")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcbalance", type=("build", "run"))
