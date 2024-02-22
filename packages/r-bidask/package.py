# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBidask(RPackage):
	"""Efficient Estimation of Bid-Ask Spreads from Open, High, Low,
and Close Prices

	Implements an efficient estimator of bid-ask spreads from open, high, low, and close prices
  as described in Ardia, Guidotti, & Kroencke (2021) <https://www.ssrn.com/abstract=3892335>. 
  It also provides an implementation of the estimators described in 
  Roll (1984) <doi:10.1111/j.1540-6261.1984.tb03897.x>, 
  Corwin & Schultz (2012) <doi:10.1111/j.1540-6261.2012.01729.x>,
  and Abdi & Ranaldo (2017) <doi:10.1093/rfs/hhx084>.
	"""
	
	homepage = "https://github.com/eguidotti/bidask"
	cran = "bidask" 

	version("2.0.2", md5="4cd6b8743d961502e986ee491b5f0ee3")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
