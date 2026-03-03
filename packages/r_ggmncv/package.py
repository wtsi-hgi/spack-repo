# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmncv(RPackage):
	"""Gaussian Graphical Models with Nonconvex Regularization

	Estimate Gaussian graphical models with nonconvex penalties <doi:10.31234/osf.io/ad57p>, 
  including the atan Wang and Zhu (2016) <doi:10.1155/2016/6495417>, 
  seamless L0 Dicker, Huang, and Lin (2013) <doi:10.5705/ss.2011.074>,
  exponential Wang, Fan, and Zhu <doi:10.1007/s10463-016-0588-3>, 
  smooth integration of counting and absolute deviation Lv and Fan (2009) <doi:10.1214/09-AOS683>,
  logarithm Mazumder, Friedman, and Hastie (2011) <doi:10.1198/jasa.2011.tm09738>,
  Lq, smoothly clipped absolute deviation Fan and Li (2001) <doi:10.1198/016214501753382273>,
  and minimax concave penalty Zhang (2010) <doi:10.1214/09-AOS729>. There are also extensions
  for computing variable inclusion probabilities, multiple regression coefficients, and 
  statistical inference <doi:10.1214/15-EJS1031>.
	"""
	
	cran = "GGMncv" 

	version("2.1.1", md5="cf6845b7bd9590f7e705c8685f37032e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@0.11.1:", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggally@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-glassofast@1:", type=("build", "run"))
	depends_on("r-network@1.15:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
	depends_on("r-mathjaxr@1.0.1:", type=("build", "run"))
	depends_on("r-mass@7.3.51.5:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-sna@2.5:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
